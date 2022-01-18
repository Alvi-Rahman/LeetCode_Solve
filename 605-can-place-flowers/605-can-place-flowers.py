class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flag = False
        
        if sum(flowerbed) + n <2:
            return True
        for i in range(1, len(flowerbed)-1):
            
            if flowerbed[0] == flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            if flowerbed[-1] == flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1
            elif flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            if n < 1:
                flag = True
                break
        return flag
            