import typing

from chessengine.utils.board import is_valid_position

from .piece import Piece

if typing.TYPE_CHECKING:
    from chessengine.board import Board


class Knight(Piece):
    @staticmethod
    def notation() -> str:
        return "n"

    def is_move_valid(self, board: "Board", from_: tuple[int, int], to: tuple[int, int]) -> bool:
        self.check_self(board, from_)

        if not self.is_empty_or_can_take(board, to):
            return False

        x, y = abs(from_[0] - to[0]), abs(from_[1] - to[1])

        return set([x, y]) == set([1, 2])

    def get_valid_moves(self, board: "Board", position: tuple[int, int]) -> list[tuple[int, int]]:
        self.check_self(board, position)

        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        result = []

        for direction in directions:
            to = (position[0] + direction[0], position[1] + direction[1])

            if not is_valid_position(to):
                continue

            if not self.is_empty_or_can_take(board, to):
                continue

            result.append(to)

        return result
