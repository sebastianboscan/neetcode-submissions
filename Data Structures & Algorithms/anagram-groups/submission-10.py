class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # {alphabetArr:[word1, word2, ...]}
        res = defaultdict(list)

        for i, n in enumerate(strs):

            alphabetArr = [0] * 26
            
            for c in strs[i]:
                alphabetArr[ord(c) - ord("a")] += 1
            
            res[tuple(alphabetArr)].append(n)

        return list(res.values())
        