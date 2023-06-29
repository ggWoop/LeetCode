class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        #hint: 두 점을 이용하여 직선의 기울기와 절편을 먼저 구하고, 나머지 점들이 직선 위에 위치하는지 체크하면 쉽게 풀립니다. 단, 예외 상황이 있으니 이를 잘 고려해보세요
        

       
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            
            # 기울기 계산
            if (y2 - y1) * (x - x1) != (y - y1) * (x2 - x1):
                return False
        
        return True

        





            # x1 = 0
            # y1 = 0
            # count = 0

            # for i in range(len(coordinates)):
            #     x1 = coordinates[i][0]
            #     y1 = coordinates[i][1]
                
            #     if i ==0:
            #         pass
            #         if x1 - y1 != -1 and 1:
            #             return False

                
            # return True 


