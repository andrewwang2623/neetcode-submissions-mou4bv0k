class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = {}
        listt = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in lists:
                lists[i] += 1
            else:
                lists[i] = 1
        for i in t:
            if i in listt:
                listt[i] += 1
            else:
                listt[i] = 1
        return lists == listt