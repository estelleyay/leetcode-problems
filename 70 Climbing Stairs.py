class Solution(object):
    def combinantion(self, n, k) -> float:
        res = 1
        for i in range(k):
            res = res * (n-i)
        for i in range(k):
            res = res / (i+1)
        return res

    def climbStairs(self, n) -> int:
        """
        :type n: int
        :rtype: int
        """
        sum = 0

        for i in range(n // 2 + 1):
            sum = sum + self.combinantion(n-i, i)  # sum = sum + math.comb(n-i, i)

        return sum
