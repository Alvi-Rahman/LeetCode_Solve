class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        i = 0
        for j in s:   
            
            if j == "(":
                stack.append(i)
            elif j == ")" and len(stack) > 0:
                stack.pop()
            
            elif j == ")" and len(stack) <= 0:
                s = s[:i] + s[i+1:]
                continue
                
            i += 1
                
        
        while stack:
            i = stack.pop()
            s = s[:i] + s[i+1:]
            
            
        return s