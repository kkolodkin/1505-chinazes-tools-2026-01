
import html
import random
import requests


def run():
    url = "https://opentdb.com/api.php?amount=5&type=multiple"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("response_code") != 0:
            print("Не удалось получить вопросы.")
            return

        questions = data["results"]
        score = 0

        print("\n=== Quiz Game ===")

        for number, question in enumerate(questions, start=1):
            question_text = html.unescape(question["question"])
            correct_answer = html.unescape(question["correct_answer"])

            answers = [
                html.unescape(answer)
                for answer in question["incorrect_answers"]
            ]
            answers.append(correct_answer)

            random.shuffle(answers)

            print(f"\nQuestion {number}: {question_text}")

            for index, answer in enumerate(answers, start=1):
                print(f"{index}. {answer}")

            user_answer = input("Your answer (1-4): ").strip()

            if user_answer in ("1", "2", "3", "4"):
                selected_answer = answers[int(user_answer) - 1]

                if selected_answer == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer: {correct_answer}")
            else:
                print(f"Invalid answer. Correct answer: {correct_answer}")

        print(f"\nYour score: {score}/{len(questions)}")

    except requests.RequestException as error:
        print(f"API error: {error}")
    except (ValueError, KeyError) as error:
        print(f"Error processing API response: {error}")
