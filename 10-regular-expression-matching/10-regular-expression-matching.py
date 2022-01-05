class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.parse_chars(s, p, len(s)-1, len(p)-1)
    
    def parse_chars(self, s, p, i, j):
        if i == j == -1:
            return True

        if j < 0:
            return False

        if i < 0:
            return p[j]=="*" and self.parse_chars(s, p, i, j-2)

        if p[j] == "*":
            if self.parse_chars(s, p, i, j-2): 
                return True

            if (p[j-1] == "." or s[i] == p[j-1]) and self.parse_chars(s, p, i-1, j):   
                return True

        elif (p[j] == "." or p[j] == s[i]) and self.parse_chars(s, p, i-1, j-1):
            return True

        return False