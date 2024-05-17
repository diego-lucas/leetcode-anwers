class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        middle = int(len(x_str) / 2)
        index_rev = 0

        for index in range(0, middle):
            index_rev -= 1
            if x_str[index] != x_str[index_rev]:
                return False
        return True
