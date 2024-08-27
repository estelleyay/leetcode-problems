# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
#     return False if version is good, True if version is bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        res = self.recurse_to_find(start, end)
        return res

    def recurse_to_find(self, start: int, end: int) -> int:
        mid = (start + end)//2
        dif = end - start + 1
        while dif > 3:
            if isBadVersion(mid) == True:
                end = mid
                return self.recurse_to_find(start, end)
            if isBadVersion(mid) == False:
                start = mid + 1
                return self.recurse_to_find(start, end)

        if isBadVersion(start) == False:
            if isBadVersion(mid) == False:
                return end
            return mid
        return start

