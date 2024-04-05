from collections.abc import Iterator


def summary_ranges(nums: list[int]) -> list[str]:
    n = len(nums)
    if n == 0:
        return []

    def ranges() -> Iterator[tuple[int, int]]:
        start = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                continue
            yield nums[start], nums[i - 1]
            start = i
        yield nums[start], nums[n - 1]

    out = list[str]()
    for start, end in ranges():
        if start == end:
            out.append(str(start))
        else:
            out.append(f"{start}->{end}")
    return out


def test_example1() -> None:
    assert summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]


def test_example2() -> None:
    assert summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
