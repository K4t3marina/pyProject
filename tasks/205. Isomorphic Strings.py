# Given two strings s and t, determine if they are isomorphic
#  task from leetcode - 205. Isomorphic Strings

class Solution():
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def isIsomorphic(self):
        d1, d2 = {}, {}
        for i in range(len(s)):
            ls, lt = self.s[i], self.t[i]
            if ls not in d1:
                d1[ls] = lt
            if lt not in d2:
                d2[lt] = ls
            if d1[ls] != lt or d2[lt] != ls:
                return False
        return True


s = 'paper'
t = 'title'
sol = Solution(s, t)
print(sol.isIsomorphic())