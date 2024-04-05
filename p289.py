# Use bit 1 to store pre-update state.
WAS_ALIVE = 0b10


def life(m: list[list[int]]) -> None:
    height = len(m)
    width = len(m[0])

    def neighbors(r0: int, c0: int) -> int:
        count = 0
        for r in (r0 - 1, r0, r0 + 1):
            for c in (c0 - 1, c0, c0 + 1):
                if r == r0 and c == c0:
                    continue
                if r < 0 or r >= height or c < 0 or c >= width:
                    continue
                if m[r][c] & WAS_ALIVE:
                    count += 1
        return count

    # Shift pre-update state into second bit
    for r in range(height):
        for c in range(width):
            m[r][c] <<= 1

    for r in range(height):
        for c in range(width):
            count = neighbors(r, c)
            if m[r][c] & WAS_ALIVE:
                if count == 2 or count == 3:
                    m[r][c] |= 1
            else:
                if count == 3:
                    m[r][c] |= 1

    # Retain only first bit
    for r in range(height):
        for c in range(width):
            m[r][c] &= 1
