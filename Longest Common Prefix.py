class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        flag = 1
        
        if(strs == []):
            return common
        else:
            lens = len(strs[0])
        for k in range(1,len(strs)):
            if len(strs[k])<lens : 
                lens = len(strs[k])
        for i in range(lens):
            check = strs[0][i]
            for j in range(1,len(strs)):
                if(strs[j][i] != check):
                    flag = 0
                    break
            if(flag == 1):
                common = common + check
                
        return common