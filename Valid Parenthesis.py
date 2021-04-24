class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"[":"]", "{":"}", "(":")", "]":0, "}":0, ")":0}
        openB = ["{","(","["]
                
        for b in s:
            if(b in openB):
                stack.append(b)
            elif(len(stack) != 0):
                if(b == pair[stack.pop()]):
                    continue
                else:
                    return False
            else:
                return False

        if(stack == []):
            return True
        else:
            return False