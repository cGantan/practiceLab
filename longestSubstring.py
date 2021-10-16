#question from LeetCode
# Given a string s, find the length of the longest substring without repeating characters.
# Example
# Input: s = pwwkew
# Output: 3
# Input: s = bbbbb
# Output: 1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #initial approach: had errors in detecting for something like "aab"
        """
        seen = {}
        max_len = 0
        seen_before = False
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                if (max_len == 0):
                    max_len = 1
            else:
                seen_before = True
                if (max_len < i - seen[s[i]]):
                    max_len = i - seen[s[i]]
                seen[s[i]] = i
        return max_len
        """

        #window method referenced from GeeksforGeeks
        if len(s) < 2:
            return len(s)
        res = ""
        max_len = -1
        for i in range(len(s)):
            if s[i] in res:
                res = res[res.index(s[i]) + 1:]
            res = res + s[i]
            max_len = max(max_len, len(res))
        return max_len
