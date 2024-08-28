def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    dic_magazine = {}

    for char in magazine:
        if char not in dic_magazine:
            dic_magazine[char] = 0
        dic_magazine[char] += 1

    for char in ransomNote:
        if char in dic_magazine:
            if dic_magazine[char] > 0:
                dic_magazine[char] -= 1
                continue
            return False
        return False
    return True
