def maxSubArray(self, nums: list[int]) -> int:
    maxsum = nums[0]
    cur_max = nums[0]

    for i in range(1, len(nums)):
        cur_max = max(cur_max + nums[i], nums[i])
        maxsum = max(maxsum, cur_max)

    return maxsum
