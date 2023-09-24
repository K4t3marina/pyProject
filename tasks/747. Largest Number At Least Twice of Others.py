# 747. Largest Number At Least Twice of Others
# my solution of a task from leetcode

nums = [3, 6, 1, 0]


class Solution(object):

    def dominant_index(self) -> int:
        old_nums = nums[:]
        nums.sort()
        m = nums[-1]
        return old_nums.index(m) if nums.pop() >= nums.pop() * 2 else -1


sol = Solution()
print(sol.dominant_index())
