from p383 import can_construct


def test_example1() -> None:
    assert not can_construct("a", "b")


def test_example2() -> None:
    assert not can_construct("aa", "ab")


def test_example3() -> None:
    assert can_construct("aa", "aab")
