class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        first, second, third = 0, 1, 1

        for i in range(n - 3):
            first, second, third = second, third, first + second + third

        return first + second + third