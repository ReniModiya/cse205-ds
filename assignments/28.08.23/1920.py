class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        index = [0]*len(nums)
        for element in nums:
            index[element] = nums[nums[element]]
        return index
            
            