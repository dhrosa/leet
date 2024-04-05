def two_sum(nums: list[int], target: int) -> list[int]:
    indexes = dict[int, int]()
    for i, n in enumerate(nums):
        if (j := indexes.get(target - n)) is not None:
            return [j, i]
        indexes[n] = i
    assert False


def test_example1() -> None:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
