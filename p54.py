def spiral_order(matrix: list[list[int]]) -> list[int]:
    bottom = len(matrix)
    right = len(matrix[0])

    top = 0
    left = 0

    values = list[int]()
    while True:
        # NW -> NE
        for c in range(left, right):
            values.append(matrix[top][c])
        top += 1
        if top == bottom:
            break

        # NE -> SE
        for r in range(top, bottom):
            values.append(matrix[r][right - 1])
        right -= 1
        if right == left:
            break

        # SE -> SW
        for c in range(right - 1, left - 1, -1):
            values.append(matrix[bottom - 1][c])
        bottom -= 1
        if bottom == top:
            break

        # SW -> NW:
        for r in range(bottom - 1, top - 1, -1):
            values.append(matrix[r][left])
        left += 1
        if left == right:
            break

    return values
