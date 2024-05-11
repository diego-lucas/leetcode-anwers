from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []
        for i in arr:
            for j in arr:
                if i >= j:
                    continue
                fractions.append(((i,j), i/j))
        fractions_sorted = sorted(fractions, key=lambda x:x[1])
        return list(fractions_sorted[k-1][0])

