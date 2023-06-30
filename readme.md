# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players, X and O, to take turns and compete against each other to win.

## How to Play

1. X starts the game.
2. According to the board below, choose your tile (1-9).
3. Players take turns until the game ends.

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

The game will display the current state of the board after each move. The game ends when a player wins, or it's a tie.

## Game Rules

- The game starts with X making the first move.
- Players take turns placing their symbol (X or O) on an available tile.
- A player wins if they have three of their symbols in a horizontal, vertical, or diagonal row.
- If all tiles are filled and no player has won, it's a tie.

## Prerequisites

The following dependencies are required to run the game:

- `colorama`: Used for console text colors.
- `time`: Used for adding a delay between moves.

Make sure you have these libraries installed before running the game.

## How to Run

To start the game, run the Python script. The game will display the rules, initialize the board, and begin the game loop. Players will be prompted to select a tile by entering a number between 1 and 9.

```python
python tic_tac_toe.py
```

Enjoy playing Tic Tac Toe!
