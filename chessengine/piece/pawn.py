import typing
from typing import Optional

from chessengine.color import Color
from chessengine.utils.board import is_valid_position

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

    def _get_en_passant(self, board: "Board", position: tuple[int, int]) -> Optional[tuple[int, int]]:
        last_move_piece, last_move_from, last_move_to = board.history[-1]

        # last move should be from a pawn and should be two squares (first move)
        if not isinstance(last_move_piece, Pawn):
            return None
        if abs(last_move_to[1] - last_move_from[1]) != 2:
            return None

        # last move should be level vertically and adjacent to self
        if abs(last_move_to[0] - position[0]) != 1:
            return None
        if last_move_to[1] != position[1]:
            return None

        # en passant is possible, return destination of self
        return (last_move_to[0], position[1] + self._direction)

    def is_en_passant(self, board: "Board", from_: tuple[int, int], to: tuple[int, int]):
        en_passant_to = self._get_en_passant(board, from_)

        return en_passant_to == to

    def is_move_valid(self, board: "Board", from_: tuple[int, int], to: tuple[int, int]) -> bool:
        self.check_self(board, from_)

        vertical_diff = to[1] - from_[1]
        vertical_length = abs(vertical_diff)
        vertical_direction = vertical_diff / vertical_length

        if vertical_direction != self._direction:
            return False

        if to[0] != from_[0]:
            if abs(to[0] - from_[0]) != 1:
                return False

            if vertical_length != 1:
                return False

            square = board.at(to)

            if square is not None and square.color != self.color:
                # normal take
                return True

            if len(board.history) == 0:
                return False

            return self.is_en_passant(board, from_, to)

        if from_[1] == self._start_square:
            # first move
            return 1 <= vertical_length <= 2

        # normal move
        return vertical_length == 1

    def get_valid_moves(self, board: "Board", position: tuple[int, int]) -> list[tuple[int, int]]:
        result = []

        forward = (position[0], position[1] + self._direction)
        if board.at(forward) is None:
            # normal move
            result.append(forward)

        double_forward = (forward[0], forward[1] + self._direction)
        if position[1] == self._start_square and board.at(double_forward) is None:
            # first move
            result.append(double_forward)

        for direction in [(-1, self._direction), (1, self._direction)]:
            # normal take
            target = (position[0] + direction[0], position[1] + direction[1])
            if not is_valid_position(target):
                continue

            square = board.at(target)

            if square is not None and square.color != self.color:
                result.append(target)

        en_passant = self._get_en_passant(board, position)

        if en_passant is not None:
            result.append(en_passant)

        return result
