from typing import List
#
# [["bat"],["nat","tan"],["ate","eat","tea"]]

# a = []
# for i in strs:
#     s = {}
#     for j in i:
#         if j not in s:
#             s[j] = 1
#         s[j] += 1
#     a.append(s)
# r = [] print(a, a[0]==a[1], r)
# ----------------------------------------------------
# r = []
# new_strs = [sorted(i) for i in strs]
# while len(strs) != 0:
#     el = new_strs[0]
#     count_el = new_strs.count(el)
#     if count_el == 1:
#         r.append([strs[0]])
#         strs.remove(strs[0])
#         new_strs.remove(el)
#     else:
#         li = []
#         for j in range(count_el):
#             id = new_strs.index(el)
#             li.append(strs[id])
#             strs.pop(id)
#             new_strs.pop(id)
#         r.append(li)
#
#
# print(r)
class Solution():

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s in di:
                di[s].append(strs[i])
            else:
                di[s] = [strs[i]]
        return [v for v in di.values()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))