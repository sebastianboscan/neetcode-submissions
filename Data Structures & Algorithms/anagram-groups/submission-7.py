class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # {alphabetArr:[word1, word2, ...]}
        res = {}

        for i, n in enumerate(strs):

            alphabetArr = [0] * 26
            
            for j, c in enumerate(strs[i]):
                alphabetArr[ord(c) - ord("a")] += 1
            
            tuple_ph = tuple(alphabetArr)
            res[tuple_ph] = res.get(tuple_ph, [])
            res[tuple_ph].append(n)

        return list(res.values())
        