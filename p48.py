def transpose(m: list[list[int]]) -> None:
    n = len(m)
    for r in range(n):
        for c in range(r, n):
            a, b = m[r][c], m[c][r]
            m[r][c], m[c][r] = b, a


def flip(m: list[list[int]]) -> None:
    n = len(m)
    for row in m:
        for c in range(n // 2):
            a, b = row[c], row[n - c - 1]
            row[n - c - 1], row[c] = a, b


def rotate(matrix: list[list[int]]) -> None:
    transpose(matrix)
    flip(matrix)
