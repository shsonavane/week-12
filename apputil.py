import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    """
    Execute one step of Conway's Game of Life.
    
    Rules:
    - Any live cell with 2-3 live neighbors survives
    - Any dead cell with exactly 3 live neighbors becomes alive
    - All other cells die or stay dead
    
    Parameters
    ----------
    current_board : numpy.ndarray
        A binary array where 1 represents a living cell and 0 represents a dead cell.
    
    Returns
    -------
    updated_board : numpy.ndarray
        The board after one step of the game.
    """
    # Get dimensions of the board
    rows, cols = current_board.shape
    
    # Create a new board for the next generation
    updated_board = np.zeros_like(current_board)
    
    # Iterate through each cell
    for i in range(rows):
        for j in range(cols):
            # Count live neighbors (8 surrounding cells)
            # We use modulo (%) to wrap around edges (toroidal topology)
            neighbors = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    # Skip the cell itself
                    if di == 0 and dj == 0:
                        continue
                    # Count neighbor with wrapping
                    ni = (i + di) % rows
                    nj = (j + dj) % cols
                    neighbors += current_board[ni, nj]
            
            # Apply Conway's Game of Life rules
            if current_board[i, j] == 1:  # Cell is currently alive
                if neighbors == 2 or neighbors == 3:
                    updated_board[i, j] = 1  # Cell survives
                else:
                    updated_board[i, j] = 0  # Cell dies (underpopulation or overpopulation)
            else:  # Cell is currently dead
                if neighbors == 3:
                    updated_board[i, j] = 1  # Cell becomes alive (reproduction)
                else:
                    updated_board[i, j] = 0  # Cell stays dead

    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. 
        In this array, 1 represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)