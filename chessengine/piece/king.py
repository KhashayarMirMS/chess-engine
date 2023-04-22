import typing

from .piece import Piece

if typing.TYPE_CHECKING:
    from chessengine.board import Board


class King(Piece):
    @staticmethod
    def notation() -> str:
        return "k"

    def is_move_valid(self, board: "Board", from_: tuple[int, int], to: tuple[int, int]) -> bool:
        # TODO
        return super().is_move_valid(board, from_, to)

    def get_valid_moves(self, board: "Board", position: tuple[int, int]) -> list[tuple[int, int]]:
        # TODO
        return super().get_valid_moves(board, position)
