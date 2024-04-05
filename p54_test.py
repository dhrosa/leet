import pytest

from p54 import spiral_order

cases = [
    (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
    ),
]
pytestmark = pytest.mark.parametrize("matrix,expected", cases)


def test_p54(matrix: list[list[int]], expected: list[int]) -> None:
    assert spiral_order(matrix) == expected
