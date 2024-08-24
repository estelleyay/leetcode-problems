def search(self, nums: List[int], target: int) -> int:
    startIndex = 0
    endIndex = len(nums) - 1
    while startIndex <= endIndex:
        mid = (startIndex + endIndex) // 2
        mid_val = nums[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            startIndex = mid + 1
        else:
            endIndex = mid - 1
    return -1
