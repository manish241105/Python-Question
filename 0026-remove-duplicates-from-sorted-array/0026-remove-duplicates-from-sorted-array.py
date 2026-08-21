class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
nums = [0,0,1,1,1,2,2,2,3,3,3,3,3]
expectedNums = [0,1,2,3]

sol = Solution()
k = sol.removeDuplicates(nums)

assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]

print("Passed! k =", k)