from p289 import life


def test_example1() -> None:
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    life(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
