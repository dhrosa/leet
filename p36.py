from collections.abc import Iterator
from itertools import product, repeat
from typing import TypeAlias

Index: TypeAlias = tuple[int, int]


def is_valid(board: list[list[str]]) -> bool:
    def regions() -> Iterator[Iterator[Index]]:
        # Row regions
        for row in range(0, 9):
            yield zip(repeat(row), range(9))
        # Column regions
        for col in range(0, 9):
            yield zip(range(9), repeat(col))
        # Square regions
        for square_row, square_col in product(range(3), range(3)):
            start_row = square_row * 3
            start_col = square_col * 3
            yield product(
                range(start_row, start_row + 3), range(start_col, start_col + 3)
            )

    for region in regions():
        filled_values = [v for (r, c) in region if (v := board[r][c]) != "."]
        if len(set(filled_values)) != len(filled_values):
            return False

    return True
