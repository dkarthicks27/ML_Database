class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)
        if k >= tot:
            if k % tot == 0:
                return 0
            else:
                rem = k % tot
                for i in range(len(chalk)):
                    if rem >= chalk[i]:
                        rem -= chalk[i]
                    else:
                        return i

        else:
            for i in range(len(chalk)):
                if k >= chalk[i]:
                    k -= chalk[i]
                else:
                    return i