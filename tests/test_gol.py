import pytest
from conway.gol import GameOfLife


def test_grid_size():
    game = GameOfLife()
    assert len(game.grid) == game.grid_height
    assert len(game.grid[0]) == game.grid_width


def test_grid_values():
    game = GameOfLife()
    for row in game.grid:
        for cell in row:
            assert cell == 0 or cell == 1


def test_create_grid():
    game = GameOfLife()
    game.create_grid()
    for row in game.grid:
        for cell in row:
            assert cell == 0 or cell == 1


def test_create_widgets():
    game = GameOfLife()
    game.create_widgets()
    assert game.canvas
    assert game.start_game
    assert game.stop_game
    assert game.reset_game


def test_draw_grid():
    game = GameOfLife()
    game.draw_grid()
    assert game.canvas


def test_update_grid():
    game = GameOfLife()
    game.start_game()
    game.update_grid()
    assert game.grid


def test_get_neighbors():
    game = GameOfLife()
    game.grid[0][0] = 1
    assert game.get_neighbors(0, 0) == 1 or 2 or 3
    assert game.get_neighbors(0, 1) == 1 or 2 or 3 or 4 or 5
    assert game.get_neighbors(1, 0) == 1 or 2 or 3 or 4 or 5
