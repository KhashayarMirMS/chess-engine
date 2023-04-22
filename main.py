import os

from chessengine.board import Board
from chessengine.utils.print import PrintStyle


# async def main():
def main():
    os.system("clear")

    b = Board.from_starting_position()

    should_end = False
    error_text = ""

    while not should_end:
        os.system("clear")
        print(b)
        print("\n")

        if error_text != "":
            print(PrintStyle.RED + error_text + PrintStyle.NONE)
        else:
            print()

        error_text = ""

        try:
            next_command = input("> ")

            if next_command.startswith("highlight "):
                coords = next_command.replace("highlight ", "")
                b.highlight(coords)

            elif next_command.startswith("move "):
                from_, to = list(map(lambda s: s.strip(), next_command.replace("move ", "").split("->")))

                b.move(from_, to)

            elif next_command == "exit":
                should_end = True

            else:
                raise Exception("unknown command")

        except Exception as exc:
            error_text = str(exc)

        except KeyboardInterrupt:
            should_end = True


main()
