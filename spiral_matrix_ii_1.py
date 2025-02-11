
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left_border = 0
        right_border = n-1
        upper_border = 0
        bottom_border = n-1
        max_n = n*n

        res_matrix = [[0]*n for i in range(n)]

        i = 0
        j = 0 
        direction = 'right'
        cur = 1
        while cur<=max_n:
            # print("left_border:", left_border)
            # print("right_border:", right_border)
            # print("upper_border:", upper_border)
            # print("bottom_border:", bottom_border)
            # print()

            if direction=='right':
                checked = False
                while j<=right_border:
                    res_matrix[i][j]=cur
                    cur+=1
                    j+=1
                    checked = True
                if checked:
                    j-=1

                i+=1
                direction = 'down'
                upper_border+=1

            elif direction=='down':
                checked = False
                while i<=bottom_border:
                    res_matrix[i][j]=cur
                    cur+=1
                    i+=1
                    checked = True
                if checked:
                    i-=1
                j-=1
                direction = 'left'
                right_border-=1

            elif direction=='left':
                checked = False
                while j>=left_border:
                    res_matrix[i][j]=cur
                    cur+=1
                    j-=1
                    checked = True
                if checked:
                    j+=1

                i-=1
                direction = 'up'
                bottom_border-=1

            else: # direction='up'
                checked = False
                while i>=upper_border:
                    res_matrix[i][j]=cur
                    cur+=1
                    i-=1
                    checked = True
                if checked:
                    i+=1

                j+=1
                direction = 'right'
                left_border+=1

        return res_matrix
            

