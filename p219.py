from collections import defaultdict
from itertools import pairwise


def contains_duplicates(nums: list[int], k: int) -> bool:
    groups = defaultdict[int, list[int]](list[int])
    for i, n in enumerate(nums):
        groups[n].append(i)

    for group in groups.values():
        for i, j in pairwise(group):
            if abs(i - j) <= k:
                return True
    return False


def test_example1() -> None:
    assert contains_duplicates([1, 2, 3, 1], 3)


def test_example2() -> None:
    assert contains_duplicates([1, 0, 1, 1], 1)


def test_example3() -> None:
    assert not contains_duplicates([1, 2, 3, 1, 2, 3], 2)
