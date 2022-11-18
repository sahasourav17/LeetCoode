class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            check = False
            if n % 2 == 0:
                n /= 2
                check = True

            elif n % 3 == 0:
                n /= 3
                check = True

            elif n % 5 == 0:
                n /= 5
                check = True

            if check == False:
                return False
        return True