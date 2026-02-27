class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        numToIndex = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numToIndex:
                return [numToIndex[complement], i]

            numToIndex[num] = i