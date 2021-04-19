class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        conv = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        rev = s[::-1]
        num = conv[rev[0]]
        
        for i in range(1,len(rev)):
    
            if(rev[i] == "I"):
                if(rev[i-1] == "V" or rev[i-1] == "X"):
                    num = num - 1
                else:
                    num = num + 1
            elif(rev[i] == "X"):
                if(rev[i-1] == "L" or rev[i-1] == "C"):
                    num = num - 10
                else:
                    num = num + 10
            elif(rev[i] == "C"):
                if(rev[i-1] == "D" or rev[i-1] == "M"):
                    num = num - 100
                else:
                    num = num + 100
            else:
                num = num + conv[rev[i]]
                
        return num