class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in groups:
                groups[sort] = [s]
            else:
                groups[sort].append(s)

        return [*groups.values()]


        