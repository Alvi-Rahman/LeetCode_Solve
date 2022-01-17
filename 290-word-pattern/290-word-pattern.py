class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        
        flag = True
        if len(pattern) != len(s.split()):
            return False
        for i, j in zip(pattern, s.split()):
            if i in d:
                if d[i] != j:
                    return False
            elif j in d.values():
                return False
            else:
                d[i] = j
        return flag