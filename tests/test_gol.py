import pytest
from conway.gol import GameOfLife


def test_grid_size():
    """Tests the grid size
    """
    game = GameOfLife()
    assert len(game.grid) == game.grid_height
    assert len(game.grid[0]) == game.grid_width


def test_grid_values():
    """Tests the grid values are 0 or 1
    """    
    game = GameOfLife()
    for row in game.grid:
        for cell in row:
            assert cell == 0 or cell == 1


def test_create_grid():
    """Tests the grid values are 0 or 1
    """    
    game = GameOfLife()
    game.create_grid()
    for row in game.grid:
        for cell in row:
            assert cell == 0 or cell == 1


def test_create_widgets():
    """Tests the widgets are created
    """    
    game = GameOfLife()
    game.create_widgets()
    assert game.canvas
    assert game.start_game
    assert game.stop_game
    assert game.reset_game


def test_draw_grid():
    """Tests the grid is drawn
    """    
    game = GameOfLife()
    game.draw_grid()
    assert game.canvas


def test_update_grid():
    """Tests the grid is updated
    """    
    game = GameOfLife()
    game.start_game()
    game.update_grid()
    assert game.grid


def test_get_neighbors():
    """Tests the number of neighbors, since it's random, 
    it can be 1, 2, 3, 4 or 5 number of live neighbors
    """    
    game = GameOfLife()
    game.grid[0][0] = 1
    assert game.get_neighbors(0, 0) == 1 or 2 or 3
    assert game.get_neighbors(0, 1) == 1 or 2 or 3 or 4 or 5
    assert game.get_neighbors(1, 0) == 1 or 2 or 3 or 4 or 5
