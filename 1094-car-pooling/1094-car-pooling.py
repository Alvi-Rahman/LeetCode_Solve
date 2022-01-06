class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        track = dict()
        for trip in trips:
            for i in range(trip[1], trip[2]):
                if i not in track:
                    track[i] = 0
                track[i] += trip[0]
                
                if track[i] > capacity:
                    return False
        return True