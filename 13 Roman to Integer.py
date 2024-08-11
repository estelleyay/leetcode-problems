def romanToInt(s: str) -> int:
    """
    >>> s = 'III'
    >>> romanToInt(s)
    3
    >>> s = "LVIII"
    >>> romanToInt(s)
    58
    >>> s = "MCMXCIV"
    >>> romanToInt(s)
    1994
    >>> s = "MCMXCVI"
    >>> romanToInt(s)
    1996
    """
    dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    length = len(s)
    if length == 1:
        return dic[s]

    have_inversion_pairs = False
    i = 1
    while not have_inversion_pairs and i < length:
        if dic[s[i]] > dic[s[i - 1]]:
            have_inversion_pairs = True
        i += 1
    if not have_inversion_pairs:
        res = dic[s[0]]
        for i in range(1, length):
            res += dic[s[i]]
        return res

    else:  # have_inversion_pairs == True
        res = 0
        i = 0
        while i < length:
            cur_value = dic[s[i]]
            if i + 1 < length:  # 有下一个
                next_value = dic[s[i + 1]]
                if cur_value >= next_value:
                    res += cur_value
                    i += 1
                else:  # cur_value < next value, need to subtract
                    res += (next_value - cur_value)
                    i += 2
            else:  # 已经是最后一个，没有下一个
                res += cur_value
                i += 1
        return res
