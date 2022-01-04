class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0

        for i in range(len(s)):
            lst = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] in lst:
                    break
                lst.append(s[j])
            if len(lst) > _max:
                _max = len(lst)
                
        return _max
            