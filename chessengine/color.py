import enum


class Color(enum.Enum):
    WHITE = "white"
    BLACK = "black"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)
