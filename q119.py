class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        final = []
        for i in range(1, rowIndex + 2):
            temp = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    num = 1
                else:
                    num = final[i-2][j-1] + final[i-2][j]
                temp.append(num)
            final.append(temp)
        return final[-1]
