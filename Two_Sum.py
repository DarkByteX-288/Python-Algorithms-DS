# This line finds the sum of two numbers
"""Two Sum - Hash Map Solution
        Find two numbers in array that add up to target.
        Return their 1-based indices."""
class Solution:
    def twoSum(self, nums, target):
            # Stores numbers we have already seen with their indices
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:        # ✅ INSIDE the loop
                return [seen[complement], i]
            
            seen[num] = i
