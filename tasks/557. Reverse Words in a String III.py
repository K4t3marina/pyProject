# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# my solution of a task from leetcode

# "s'teL ekat edoCteeL tsetnoc" - needed result


class Solution():
    string = "Let's take LeetCode contest"

    def __int__(self, string):
        self.string = string

    def reverse_words(self):
        return ' '.join([i[::-1] for i in self.string.split()])


sol = Solution()
print(sol.reverse_words())