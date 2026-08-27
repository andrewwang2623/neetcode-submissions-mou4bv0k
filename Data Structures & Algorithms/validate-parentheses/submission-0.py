class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        complement = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] not in complement:
                open.append(s[i])
            else:
                if open == []:
                    return False
                if open[-1] == complement[s[i]]:
                    open.pop()
                else:
                    return False
        return open == []