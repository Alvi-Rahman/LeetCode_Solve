class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        flag = 0
        test = []
        co_ordinate = [0, 0]
        for idx in range(5):
            for i in instructions:
                if i == "G":
                    if flag == 0:
                        co_ordinate = [co_ordinate[0], co_ordinate[1] + 1]
                    elif flag == 90:
                        co_ordinate = [co_ordinate[0] + 1, co_ordinate[1]]
                    elif flag == 180:
                        co_ordinate = [co_ordinate[0], co_ordinate[1] - 1]
                    elif flag == 270:
                        co_ordinate = [co_ordinate[0] - 1, co_ordinate[1]]

                elif i == "L":
                    flag = (flag - 90 +360) % 360
                elif i == "R":
                    flag = (flag + 90 +360) % 360
            
            if idx == 0 or idx == 4:
                test.append(co_ordinate)
            
        if test[0] == test[1]:
            return True
        return False