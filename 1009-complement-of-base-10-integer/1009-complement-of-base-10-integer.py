class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(("{0:b}".format(n)).replace('0','b').replace('1',        
                    '0').replace('b','1'),2)