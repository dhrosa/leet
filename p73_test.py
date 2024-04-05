from p73 import set_matrix_zeroes


def test_example1() -> None:
    matrix: list[list[int | None]] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_matrix_zeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_case2() -> None:
    matrix: list[list[int | None]] = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_matrix_zeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
