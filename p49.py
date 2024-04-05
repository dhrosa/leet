from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    mapping = defaultdict[str, list[str]](list)
    for s in strs:
        mapping["".join(sorted(s))].append(s)
    return list(mapping.values())


def test_example1() -> None:
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
