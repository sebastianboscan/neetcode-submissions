class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # {alphabetArr:[word1, word2, ...]}
        res = {}

        for i, n in enumerate(strs):

            alphabetArr = [0] * 26
            
            for j, c in enumerate(strs[i]):
                alphabetArr[ord(c) - ord("a")] += 1
            
            res[tuple(alphabetArr)] = res.get(tuple(alphabetArr), [])
            res[tuple(alphabetArr)].append(n)

        return list(res.values())
        