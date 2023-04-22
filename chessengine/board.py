from typing import Optional, cast

from chessengine.color import Color
from chessengine.piece import Piece, all_pieces
from chessengine.utils.board import Coords, get_coords_as_tuple
from chessengine.utils.pgn import square_to_pgn
from chessengine.utils.print import PrintStyle
from chessengine.utils.string import is_upper


def _parse_fen_piece(piece: str) -> Optional[Piece]:
    color = Color.WHITE if is_upper(piece) else Color.BLACK
    piece = piece.lower()
    for piece_type in all_pieces:
        if piece_type.notation() == piece:
            return piece_type(color)

    return None


def _is_digit(s: str):
    return "1" <= s <= "9"


class Board:
    STARTING_POSITION_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    def __init__(self) -> None:
        self.squares: list[list[Optional[Piece]]] = [[None] * 8 for _ in range(8)]
        self._highlight_moves_for: Optional[tuple[int, int]] = None
        self.turn = Color.WHITE

    def from_fen(self, fen: str, turn=Color.WHITE):
        self.turn = turn

        row = 7
        for row_str in fen.split("/"):
            col = 0
            for ch in row_str:
                if _is_digit(ch):
                    col += int(ch)
                    continue

                self.squares[col][row] = _parse_fen_piece(ch)
                col += 1

            row -= 1

    @staticmethod
    def from_starting_position():
        b = Board()
        b.from_fen(Board.STARTING_POSITION_FEN)
        return b

    def does_player_own(self, position: Coords):
        square = self.at(position)

        return square is not None and square.color == self.turn

    def highlight(self, position: Coords):
        if not self.does_player_own(position):
            raise Exception("not your piece")

        self._highlight_moves_for = get_coords_as_tuple(position)

    def at(self, position: Coords):
        position = get_coords_as_tuple(position)

        return self.squares[position[0]][position[1]]

    def move(self, from_: Coords, to: Coords):
        # TODO probably store somewhere if a piece has been taken and add support for
        # castling, promotion, en passant
        if not self.does_player_own(from_):
            raise Exception("invalid square")

        from_ = get_coords_as_tuple(from_)
        to = get_coords_as_tuple(to)

        from_square = cast(Piece, self.at(from_))

        if not from_square.is_move_valid(self, from_, to):
            raise Exception("invalid move")

        self.squares[to[0]][to[1]] = from_square
        self.squares[from_[0]][from_[1]] = None

        self._highlight_moves_for = None
        self.turn = Color.BLACK if self.turn == Color.WHITE else Color.WHITE

    def get_valid_moves(self, position: Coords, *, as_pgn=False):
        position = get_coords_as_tuple(position)
        square = self.at(position)

        if square is None:
            return []

        result = square.get_valid_moves(self, position)

        if as_pgn:
            result = list(map(square_to_pgn, result))

        return result

    def __str__(self) -> str:
        highlighted_squares = self.get_valid_moves(self._highlight_moves_for) if self._highlight_moves_for else []
        squares_str = ""

        for row in range(7, -1, -1):
            row_str = f"{8 - row} | "
            for column in range(8):
                position = (column, row)
                square = self.at(position)

                if position in highlighted_squares:
                    row_str += PrintStyle.HIGHLIGHT

                if self._highlight_moves_for and position == self._highlight_moves_for:
                    row_str += PrintStyle.BLINK + PrintStyle.UNDERLINE

                if square is None:
                    row_str += " "

                else:
                    if square.color == Color.BLACK:
                        row_str += PrintStyle.BLUE

                    row_str += str(square)

                row_str += " " + PrintStyle.NONE

            row_str += "|"

            if row > 0:
                row_str += "\n"

            squares_str += row_str

        return "  " + ("-" * 19) + " " + "\n" + squares_str + "\n  " + ("-" * 19) + "\n    a b c d e f g h"
