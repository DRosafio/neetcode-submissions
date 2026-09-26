class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)

        for i in strs:
            m=''.join(sorted(i))
            if m not in x:
                x[m] = [i]
            else:
                x[m].append(i)
        return list(x.values())
