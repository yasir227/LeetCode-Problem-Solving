class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c = cost
        c.append(0)

        for i in range(len(c) - 3, -1, -1):
            c[i] += min(c[i + 1], c[i + 2])
        return min(c[0], c[1])