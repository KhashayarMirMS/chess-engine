from typing import Union, cast

from chessengine.utils.pgn import pgn_to_square


def is_valid_position(position: tuple[int, int]):
    return 0 <= position[0] < 8 and 0 <= position[1] < 8


Coords = Union[tuple[int, int], str]


def get_coords_as_tuple(coords: Coords):
    if type(coords) is str:
        return pgn_to_square(coords)

    coords = cast(tuple[int, int], coords)

    return coords
