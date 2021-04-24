class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = []
        i = len(digits) - 1
        
        while(i >= 0):
            if(digits[i] == 9):
                digits[i] = 0
                if(i == 0):
                    digits = [1] + digits
                i -= 1
            else:
                digits[i] = digits[i] + 1
                break
        
        
        
        return (digits)