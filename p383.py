from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    letters = Counter(magazine)
    letters.subtract(Counter(ransom_note))
    return all(v >= 0 for v in letters.values())
