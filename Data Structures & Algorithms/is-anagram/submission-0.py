class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters: dict[str, int] = {}
        t_letters: dict[str, int] = {}

        for x in s:
            s_letters[x] = s_letters.get(x, 0) + 1

        for y in t:
            t_letters[y] = t_letters.get(y, 0) + 1

        return s_letters == t_letters