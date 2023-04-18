import enum

from chessengine.color import Color


class PieceType(enum.Enum):
    ROOK = "r"
    KNIGHT = "n"
    BISHOP = "b"
    QUEEN = "q"
    KING = "k"
    PAWN = "p"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


class Piece:
    def __init__(self, type_: PieceType, color: Color) -> None:
        self.type_ = type_
        self.color = color

    def __str__(self) -> str:
        piece = str(self.type_)

        return piece.upper() if self.color is Color.WHITE else piece

    def __repr__(self) -> str:
        return str(self)
