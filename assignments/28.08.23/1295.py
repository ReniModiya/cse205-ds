
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for element in nums:
            e = str(element)
            length = len(e)
            if  length % 2 ==0 :
                count+= 1
        return count
        