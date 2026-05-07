class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in sublists:
                sublists[sorted_string].append(string)
            else:
                sublists[sorted_string] = [string]
        sublists_list = []
        for i in sublists:
            sublists_list.append(sublists[i])
        return sublists_list