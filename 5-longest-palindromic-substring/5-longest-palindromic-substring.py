class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        _max = 0
        _max_str = ""
        flag = False
        for i in range(len(s)):
            for j in range(len(s)-1,-1,-1):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if _max < (j-i+1):
                        _max = (j-i)+1
                        _max_str = s[i:j+1]
                        flag = True
                    break
            if abs(i - j) > 500 and flag:
                break
        
        return _max_str
