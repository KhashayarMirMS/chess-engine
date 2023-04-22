import typing

from chessengine.utils.range import range_between

from .piece import Piece

if typing.TYPE_CHECKING:
    from chessengine.board import Board


class Rook(Piece):
    @staticmethod
    def notation() -> str:
        return "r"

    def is_move_valid(self, board: "Board", from_: tuple[int, int], to: tuple[int, int]) -> bool:
        self.check_self(board, from_)

        if from_[0] != to[0] and from_[1] != to[1]:
            return False

        if not self.is_empty_or_can_take(board, to):
            return False

        if from_[0] == to[0]:
            squares_to_check = [(from_[0], i) for i in range_between(from_[1], to[1])]
        else:
            squares_to_check = [(i, from_[1]) for i in range_between(from_[0], to[0])]

        return Piece.is_range_empty(board, squares_to_check)

    def get_valid_moves(self, board: "Board", position: tuple[int, int]) -> list[tuple[int, int]]:
        self.check_self(board, position)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        return Piece.get_valid_squares_in_directions(board, self.color, position, directions)
