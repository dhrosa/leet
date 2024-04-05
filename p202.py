def is_happy(n: int) -> bool:
    seen = set[int]()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return True


def test_example1() -> None:
    assert is_happy(19)


def test_example2() -> None:
    assert not is_happy(2)


def test_example3() -> None:
    assert is_happy(19)
