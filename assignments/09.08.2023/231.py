class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n%2 == 0 and n >1 :
            return self.isPowerOfTwo(n//2)
        else:
            return False
        