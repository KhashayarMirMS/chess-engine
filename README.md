# Chess Engine

This project aims to create a simple chess engine that can evaluate a given position and suggest best lines according to its evaluation.

## Development and installation

This project uses [poetry](https://python-poetry.org/) as its package manager. After getting poetry you can run `poetry install` to install all dependencies to run the project.

## Game Interface

You can currently run a normal game of chess in your terminal using `python main.py` after installing all the dependencies. The game will render in the terminal and has a prompt for your next command. Here's a list of available commands:

1. `move <from> -> <to>` where `from` and `to` are squares in chess notation (e.g. "e5").
2. `highlight <square>` where square in chess notation.
3. `exit`

# Todo

There are many things to be done in the project, here's a list of the most important ones:

- [ ] Pawn promotions.
- [ ] King moves (normal moves, castling).
- [ ] Checking for checks and mates.
- [ ] Disallowing illegal moves (e.g. putting yourself in check or ignoring a check).
- [ ] Support for custom positions in cli.
- [ ] Basic evaluation of the position.