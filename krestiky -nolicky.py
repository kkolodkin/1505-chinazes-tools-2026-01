
import random

def print_board(board):
    print()
    for i in range(3):
        print(" " + " | ".join(board[i * 3:i * 3 + 3]))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c]:
            return board[a]

    return None


def computer_move(board):
    for symbol in ("O", "X"):
        for i in range(9):
            if board[i] not in ("X", "O"):
                board[i] = symbol

                if check_winner(board) == symbol:
                    if symbol == "O":
                        return
                    board[i] = str(i + 1)
                    break
                else:
                    board[i] = str(i + 1)
    free_cells = [
        i for i in range(9)
        if board[i] not in ("X", "O")
    ]

    if free_cells:
        position = random.choice(free_cells)
        board[position] = "O"


def play_game():
    board = [str(i) for i in range(1, 10)]

    print("=== КРЕСТИКИ-НОЛИКИ ===")
    print("Ты играешь за X, компьютер — за O.")
    print("Выбирай клетку по номеру от 1 до 9.")

    while True:
        print_board(board)
        move = input("Твой ход: ")

        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Введи число от 1 до 9!")
            continue

        position = int(move) - 1

        if board[position] in ("X", "O"):
            print("Эта клетка уже занята!")
            continue

        board[position] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("Поздравляю! Ты победил! ")
            break

        if all(cell in ("X", "O") for cell in board):
            print_board(board)
            print("Ничья! ")
            break

        computer_move(board)
        print("Компьютер сделал ход!")

        if check_winner(board) == "O":
            print_board(board)
            print("Компьютер победил!")
            break

        if all(cell in ("X", "O") for cell in board):
            print_board(board)
            print("Ничья!")
            break


play_game()
