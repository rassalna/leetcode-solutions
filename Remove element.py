class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rep = nums.count(val)
        for _ in range(rep):
            nums.remove(val)
            
        return len(nums)