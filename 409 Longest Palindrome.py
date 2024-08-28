def longestPalindrome(s: str) -> int:
    """
    >>> s = 'ccc'
    >>> longestPalindrome(s)
    3
    >>> s = "bananas"
    >>> longestPalindrome(s)
    5
    """
    # method1: sort the string, then compare one by one
    # lst = sorted(s)
    # repeat = 0
    # i = 0
    # while i < len(lst) - 1:
    #     if lst[i] == lst[i + 1]:
    #         repeat += 2
    #         i += 2
    #     else:
    #         i += 1
    # # repeat 肯定是偶数
    # if repeat < len(lst):
    #     return repeat + 1
    # else:
    #     return repeat

    # method2: use a dictionary, improved runtime and memory
    l = len(s)
    dic = {}
    for char in s:
        if char not in dic:
            dic[char] = 0
        dic[char] += 1

    count = 0
    for key in dic:
        num = dic[key]
        if num % 2 == 0:
            count += num
        elif num > 2:  # odd
            count += (num - 1)

    if count < l:
        return count + 1
    return count
