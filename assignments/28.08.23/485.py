class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for element in nums:
            if element == 1:
                count += 1
            elif element != 1:
                count = 0 
            if count > maxi:    
                maxi = count
        return maxi

    


    

