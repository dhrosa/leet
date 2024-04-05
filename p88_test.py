from p88 import merge


def test_example1() -> None:
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def text_example3() -> None:
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    assert nums1 == [1]
