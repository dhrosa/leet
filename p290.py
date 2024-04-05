def follows_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    mapping = dict[str, str]()
    mapped_words = set[str]()
    for letter, word in zip(pattern, words):
        mapped_word = mapping.get(letter)
        if mapped_word:
            if mapped_word != word:
                return False
            continue
        if word in mapped_words:
            return False
        mapping[letter] = word
        mapped_words.add(word)
    return True


def test_example1() -> None:
    assert follows_pattern("abba", "dog cat cat dog")


def test_example2() -> None:
    assert not follows_pattern("abba", "dog cat cat fish")
