def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    length = len(s)

    tempStack = []

    for i in range (length):

        tempV = s[i]
        if tempV == '(' or tempV == '[' or tempV == '{':
            tempStack.append(tempV)
        elif len(tempStack) == 0:
            return False
        else:
            temp = tempStack.pop()
            if tempV == ')' and temp != '(':
                return False
            elif tempV == ']' and temp != '[':
                return False
            elif tempV == '}' and temp != '{':
                return False
    if len(tempStack) > 0:
        return False
    return True
