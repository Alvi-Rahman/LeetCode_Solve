class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return n and 1
        first, second, third = 0, 1, 1

        for i in range(n - 3):
            first, second, third = second, third, first + second + third

        return first + second + third