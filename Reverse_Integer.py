class Solution:
    def reverse(self, x: int) -> int:
        
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        rev = int(y)
        
        if(rev > 2 ** 31 or rev < -2 ** 32):
            return 0
        elif(x < 0):
            return -1 * rev
        else:
            return rev