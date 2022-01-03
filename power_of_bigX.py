class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0: return 1
        if n == 1: return x
        while n > 0:
            print(n)
            if n % 2 == 1:
                return x * self.myPow(x, n-1)
            if n > 1:
                res = self.myPow(x, n//2)
                res *= res
                return res
        return res

print(Solution().myPow(2, 22))
