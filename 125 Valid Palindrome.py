from curses.ascii import isalnum, isupper

from numpy.core.defchararray import lower


def isPalindrome(s: str) -> bool:
    """
    s_ = list(s)
    l = len(s_)

    for i in range(l):
        if ord(s_[i]) >= 65 and ord(s_[i]) <= 90:
            s_[i] = chr(ord(s_[i]) + 32)
    i = 0
    while i < l:
        if (ord(s_[i]) >= 48 and ord(s_[i]) <= 57) or (ord(s_[i]) >= 97 and ord(s_[i]) <= 122 ):
            i += 1
        else:
            del(s_[i])
            l -= 1
    if l == 0 or l == 1:
        return True
    else:
        com_l = l // 2
        for i in range(com_l):
            if s_[i] != s_[l - i - 1]:
                return False
        return True

    >>> s = "A man, a plan, a canal: Panama"
    >>> isPalindrome(s)
    True
    """
    length1 = len(s)
    store1 = list(s)
    store2 = []
    for i in range(length1):
        char = store1[i]
        if isalnum(char):
            if isupper(char):
                char = lower(char)
            store2.append(char)
    length2 = len(store2)
    for i in range(length2 // 2):
        store2.append(s[i])
    for j in range((length2 + 1) // 2, length2):
        if s[j] != store2.pop():
            return False
    return True

