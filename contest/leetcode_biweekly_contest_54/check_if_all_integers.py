class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        k = set(list(range(left, right + 1)))
        for li in ranges:
            st = set(list(range(li[0], li[1] + 1)))
            new = k.intersection(st)
            k = k - new

        if not k:
            return True
        else:
            return False