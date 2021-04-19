class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        output = int(y)
        
        if((x) == output):
            return True
        else:
            return False
        