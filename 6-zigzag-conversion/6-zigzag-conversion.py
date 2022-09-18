class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        import numpy as np
        from math import ceil

        zigzag_arr = np.zeros((numRows, ceil(len(s) / (numRows-1))), dtype=str)
        zigzag_arr_idx = np.zeros(numRows, dtype=int)
        mod_val = numRows - 1
        for i, c in enumerate(s):
            if int(i / mod_val) % 2 == 0:
                # Even

                idx = i % mod_val
                zigzag_arr[idx][zigzag_arr_idx[idx]] = c
                zigzag_arr_idx[idx] += 1
            else:
                idx = mod_val - (i % mod_val)
                zigzag_arr[idx][zigzag_arr_idx[idx]] = c
                zigzag_arr_idx[idx] += 1
        return "".join(i for i in zigzag_arr.flatten())