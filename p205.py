def is_isomorphic(s: str, t: str) -> bool:
    mapping = dict[str, str]()
    mapped_outputs = set[str]()
    for a, b in zip(s, t):
        mapped_a = mapping.get(a)
        if mapped_a:
            if mapped_a != b:
                return False
            continue
        if b in mapped_outputs:
            return False
        mapping[a] = b
        mapped_outputs.add(b)
    return True


def test_example1() -> None:
    assert is_isomorphic("egg", "add")


def test_example2() -> None:
    assert not is_isomorphic("foo", "bar")


def test_example3() -> None:
    assert is_isomorphic("paper", "title")


def test_case38() -> None:
    assert not is_isomorphic("badc", "baba")
