import typing

from chessengine.color import Color

from .piece import Piece

if typing.TYPE_CHECKING:
    from chessengine.board import Board


class Pawn(Piece):
    @staticmethod
    def notation() -> str:
        return "p"

    @property
    def _direction(self):
        return 1 if self.color == Color.WHITE else -1

    @property
    def _start_square(self):
        return 1 if self.color == Color.WHITE else 6

    def is_move_valid(self, board: "Board", from_: tuple[int, int], to: tuple[int, int]) -> bool:
        # TODO handle en passant
        self.check_self(board, from_)

        if to[0] != from_[0]:
            return False

        diff = to[1] - from_[1]
        move_length = abs(diff)
        move_direction = diff / move_length

        if move_direction != self._direction:
            return False

        if from_[1] == self._start_square:
            return 1 <= move_length <= 2

        return move_length == 1

    def get_valid_moves(self, board: "Board", position: tuple[int, int]) -> list[tuple[int, int]]:
        # TODO handle en passant

        result = []

        forward = (position[0], position[1] + self._direction)
        if board.at(forward) is None:
            result.append(forward)

        double_forward = (forward[0], forward[1] + self._direction)
        if position[1] == self._start_square and board.at(double_forward) is None:
            result.append(double_forward)

        return result
