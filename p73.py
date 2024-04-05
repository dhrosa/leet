def set_matrix_zeroes(m: list[list[int | None]]) -> None:
    height = len(m)
    width = len(m[0])

    def clear(target_row: int, target_col: int) -> None:
        # Clear target column
        for row in m:
            if row[target_col] != 0:
                row[target_col] = None
        # Clear target row
        for c in range(width):
            if m[target_row][c] != 0:
                m[target_row][c] = None

    for r in range(height):
        for c in range(width):
            if m[r][c] == 0:
                clear(r, c)

    for r in range(height):
        for c in range(width):
            m[r][c] = m[r][c] or 0
