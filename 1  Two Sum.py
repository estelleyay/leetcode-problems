def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length =  len(nums)

    for i in range (0, length):
        for j in range (i+1, length):
            if target == nums[i] + nums[j]:
                return [i,j]
    return None
