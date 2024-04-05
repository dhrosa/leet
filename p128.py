from dataclasses import dataclass


@dataclass
class Span:
    start: int
    """Inclusive start value"""

    end: int
    """Inclusive end value"""

    def __len__(self) -> int:
        return self.end - self.start + 1


def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    # Map values to span they are included in. Elements are only added if at any
    # point during iteration they were the endpoint of a span.
    spans: dict[int, Span] = {}

    for n in nums:
        if n in spans:
            continue
        spans[n] = Span(n, n)
        left = spans.get(n - 1)
        right = spans.get(n + 1)
        if left and right:
            # Joining two existing spans; create a new span to replace the
            # existing spans.
            span = Span(left.start, right.end)
            spans[left.start] = span
            spans[right.end] = span
        elif left:
            # Appending to an existing span
            left.end = n
            spans[n] = left
        elif right:
            # Prepending to an existing span
            right.start = n
            spans[n] = right

    return max(len(s) for s in spans.values())


def longest_consecutive2(nums: list[int]) -> int:
    unique_nums = set(nums)
    # Length of longest sequence so far
    longest = 0
    # Find starts of all sequences. A number (n) starts a sequence if (n-1) is
    # not present. This outer loop will visit each input only once.
    for start in unique_nums:
        if (start - 1) in unique_nums:
            continue
        # Found start of a sequence. Count up until (n+1) is no longer present.
        # This inner loop will only visit any given number once across the
        # entire function call, as a number can only be part of one sequence.
        end = start
        while (end + 1) in unique_nums:
            end += 1
        longest = max(longest, end - start + 1)
    return longest
