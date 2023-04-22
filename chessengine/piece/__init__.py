from typing import Type

from .bishop import Bishop as Bishop
from .king import King as King
from .knight import Knight as Knight
from .pawn import Pawn as Pawn
from .piece import Piece as Piece
from .queen import Queen as Queen
from .rook import Rook as Rook

all_pieces: list[Type[Piece]] = [
    Rook,
    Knight,
    Bishop,
    Queen,
    King,
    Pawn,
]

__all__ = [
    "Bishop",
    "King",
    "Knight",
    "Pawn",
    "Piece",
    "Queen",
    "Rook",
]
