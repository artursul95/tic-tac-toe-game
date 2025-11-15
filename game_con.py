from gameparts import Board
from gameparts import FieldIndexError, FieldNotEmptyError


def save_result(result, board):
    with open("results.txt", "a", encoding="UTF-8") as file:
        file.write(f"{result}\n")
        for row in board:
            file.write("|".join(row) + "\n")
            file.write("-" * 5 + "\n")
        file.write("\n")


def main():
    game = Board()
    game.display()
    current_player = "X"
    running = True

    while running:
        print(f"Ход делают {current_player}")

        while True:
            try:
                row = int(input("Введите номер строки: "))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input("Введите номер столбца: "))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if (row, column) in game.occupied_cell:
                    raise FieldNotEmptyError

            except FieldNotEmptyError as e:
                print(e)
            except FieldIndexError as e:
                print(e)
            except ValueError:
                print(
                    "Буквы вводить нельзя, только числа.",
                    "Пожалуйста, введите значения для строки и столбца заново.",
                    sep="\n",
                )
            except Exception as e:
                print(f"Возникла ошибка: {e}")
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            result = f"Победили {current_player}"
            print(f"{result}")
            running = False
            save_result(result, game.board)
        elif game.is_board_full():
            result = "Ничья"
            print(result)
            running = False
            save_result(result, game.board)

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
