class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_length = len(s)
        t_length = len(t)

        # 1. Check the length of both, if false then return false
        if s_length != t_length:
            return False

        # 2. Make a hasmap where key is chars and value is count of that char
        s_map = {}
        for i in range(s_length):
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1

        # 3. Same goes for t
        t_map = {}
        for i in range(t_length):
            if t[i] not in t_map:
                t_map[t[i]] = 1
            else: 
                t_map[t[i]] += 1

        # 4. Check if the hashmaps are the same
        if s_map == t_map:
            return True
        return False