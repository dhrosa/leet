from p128 import longest_consecutive2 as longest_consecutive


def test_empty() -> None:
    assert longest_consecutive([]) == 0


def test_singleton() -> None:
    assert longest_consecutive([3]) == 1


def test_non_consecutive() -> None:
    assert longest_consecutive([1, 3]) == 1


def test_consecutive() -> None:
    assert longest_consecutive([2, 3]) == 2


def test_official_0() -> None:
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_official_1() -> None:
    assert longest_consecutive([-1, 1, 2, 0]) == 4


def test_official_wat() -> None:
    # x = list(range(9000, -1000, -1))
    x = list(range(100, -100, -1))
    assert longest_consecutive(x) == len(x)
