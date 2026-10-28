class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen ={}
        for i in range (len(nums)):
            compleemt = target - nums[i]
            if compleemt in seen:
                return [i, seen [compleemt]]
            seen[nums[i]]= i