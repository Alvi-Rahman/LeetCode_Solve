class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        judge = [i+1 for i in range(n)]

        for i in (trust):
            if i[0] in judge:
                judge.remove(i[0])
        
        if not judge:
            return -1
        j = judge[0]
        for k in range(n):
            if k+1 == j:
                continue
            if [k+1, j] not in trust:
                return -1


        if judge:
            return judge[0]
        else:
            return -1
