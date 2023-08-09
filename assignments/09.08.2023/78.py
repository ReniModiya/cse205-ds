class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for i in nums:
            results += [lst + [i] for lst in results ]

        return results