from dataclasses import dataclass


@dataclass
class Entry:
    value: int
    min_value: int


class MinStack:
    def __init__(self) -> None:
        self.entries = list[Entry]()

    def push(self, val: int) -> None:
        if self.entries:
            self.entries.append(
                Entry(value=val, min_value=min(self.entries[-1].min_value, val))
            )
        else:
            self.entries.append(Entry(val, val))

    def pop(self) -> None:
        self.entries.pop()

    def top(self) -> int:
        return self.entries[-1].value

    def getMin(self) -> int:
        return self.entries[-1].min_value
