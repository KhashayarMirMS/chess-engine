import typing
from abc import ABC, abstractmethod

from chessengine.color import Color
from chessengine.utils.board import is_valid_position

if typing.TYPE_CHECKING:
    from chessengine.board import Board


class Piece(ABC):
    def __init__(self, color: Color) -> None:
        self.color = color

    def __str__(self) -> str:
        piece = self.notation()

        return piece.upper() if self.color is Color.WHITE else piece

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    @abstractmethod
    def notation() -> str:
        pass

    @abstractmethod
    def is_move_valid(self, board: "Board", from_: tuple[int, int], to: tuple[int, int]) -> bool:
        pass

    @abstractmethod
    def get_valid_moves(self, board: "Board", position: tuple[int, int]) -> list[tuple[int, int]]:
        pass

    def check_self(self, board: "Board", position: tuple[int, int]):
        if board.at(position) == self:
            return

        raise Exception("invalid board setting: move validation must originate from the piece's own square")

    def is_empty_or_can_take(self, board: "Board", position: tuple[int, int]):
        square = board.at(position)
        return square is None or square.color != self.color

    @staticmethod
    def is_range_empty(board: "Board", squares: list[tuple[int, int]]):
        for square in squares:
            if board.at(square) is not None:
                return False

        return True

    @staticmethod
    def get_valid_squares_in_directions(
        board: "Board", color: Color, start: tuple[int, int], directions: list[tuple[int, int]]
    ):
        result: set[tuple[int, int]] = set()
        for direction in directions:
            current = (start[0], start[1])
            cell = None
            while cell is None:
                result.add(current)

                current = (current[0] + direction[0], current[1] + direction[1])
                if not is_valid_position(current):
                    cell = None
                    break

                cell = board.at(current)

            if cell is not None and cell.color != color:
                result.add(current)

        result.remove(start)

        return list(result)
