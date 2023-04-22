def square_to_pgn(position: tuple[int, int]) -> str:
    return f"{chr(position[0] + ord('a'))}{position[1] + 1}"


def pgn_to_square(pgn: str) -> tuple[int, int]:
    if len(pgn) != 2:
        raise Exception(f"invalid pgn: {pgn}")

    return (ord(pgn[0]) - ord("a"), int(pgn[1]) - 1)
