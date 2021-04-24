class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        
        while(j <= len(nums)-1 and len(nums)>0):
            d = nums[i]
            if(nums[j] == d):
                nums.remove(nums[j])
            else:
                i = i+1
                j = j+1
                
        return len(nums)