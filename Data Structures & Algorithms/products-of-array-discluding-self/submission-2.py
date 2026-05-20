class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        total = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                total *= num

        for i in range(len(nums)):

            if zeroCount > 1:
                nums[i] = 0

            elif zeroCount == 1:
                nums[i] = total if nums[i] == 0 else 0

            else:
                nums[i] = total // nums[i]

        return nums