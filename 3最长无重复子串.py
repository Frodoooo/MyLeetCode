class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        chardic = {}
        maxLen = 0
        for char in list(s):
            chardic[char] = 0

        while (right < len(s)):
            chardic[s[right]] += 1
            r = s[right]
            right += 1
            while(chardic[r] > 1):
                chardic[s[left]] -= 1
                left += 1
            maxLen = max(maxLen,right - left)

        return maxLen
