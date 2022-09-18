class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        zigzag_lst = [[] for i in range(numRows)]
        mod_val = numRows - 1
        for i, c in enumerate(s):
            if int(i / mod_val) % 2 == 0:
                # Even

                idx = i % mod_val
                zigzag_lst[idx].append(c)
            else:
                idx = mod_val - (i % mod_val)
                zigzag_lst[idx].append(c)
        lst = [item for sublist in zigzag_lst for item in sublist]

        return "".join(i for i in lst)