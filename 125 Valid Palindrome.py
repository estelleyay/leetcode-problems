from numpy.core.defchararray import isalnum, isupper


def isPalindrome(s: str) -> bool:
    """
    Version 1 of the code: ascii code
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

    Version 2 of the code: stack
    length1 = len(s)
    store1 = list(s)
    store2 = []
    for i in range(length1):
        char = store1[i]
        if isalnum(char):
            if isupper(char):
                char = char.lower()
            store2.append(char)
    length2 = len(store2)
    store3 = []
    for i in range(length2 // 2):
        store3.append(store2[i])
    for j in range((length2 + 1) // 2, length2):
        if store2[j] != store3.pop():
            return False
    return True




    # Version 4 of the code: try to use logN complexity
    i = 0
    l = len(s)
    while i < l:

    don't know how
    """
    # Version 3 of the code: mutate on list,compare head to tail
    length1 = len(s)
    store1 = []
    i = 0
    while i < length1:
        char = s[i]
        if isalnum(char):
            if isupper(char):
                char = char.lower()
            store1.append(char)
        i += 1

    length2 = len(store1)

    for i in range(length2 // 2):
        if store1[i] != store1[length2 - i - 1]:
            return False
    return True
