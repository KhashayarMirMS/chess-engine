from typing import Optional

from chessengine.color import Color
from chessengine.piece import Piece, PieceType
from chessengine.utils.string import is_upper


def _parse_fen_piece(piece: str) -> Piece:
    color = Color.WHITE if is_upper(piece) else Color.BLACK
    piece = piece.lower()
    for type_ in PieceType:
        if type_.value == piece:
            return Piece(type_, color)

    return None


def _is_digit(s: str):
    return "1" <= s <= "9"


class Board:
    STARTING_POSITION_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    def __init__(self) -> None:
        self.squares: list[list[Optional[Piece]]] = [[None] * 8 for _ in range(8)]

    def from_fen(self, fen: str):
        row = 0
        for row_str in fen.split("/"):
            col = 0
            for ch in row_str:
                if _is_digit(ch):
                    col += int(ch)
                    continue

                self.squares[row][col] = _parse_fen_piece(ch)
                col += 1

            row += 1

    @staticmethod
    def from_starting_position():
        b = Board()
        b.from_fen(Board.STARTING_POSITION_FEN)
        return b

    def __str__(self) -> str:
        return (
            ("-" * 19)
            + "\n"
            + "\n".join(
                ["| " + " ".join([str(square) if square else " " for square in row]) + " |" for row in self.squares]
            )
            + "\n"
            + ("-" * 19)
        )
