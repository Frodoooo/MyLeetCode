class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chardic = {}
        for char in list(t):
            chardic[char] = 0
        charValidList = chardic.copy()
        for char in list(t):
            charValidList[char] += 1
        left = 0
        right = 0
        start = 0
        minLen = len(s) + 1
        valid = 0
        validStart = 0
        validLen = len(s) + 1
        while (right < len(s)):

            if (s[right] in chardic.keys()):
                chardic[s[right]] += 1
                if (chardic[s[right]] == charValidList[s[right]]):  #窗口中第一个符合的
                    valid += charValidList[s[right]] #符合条件的字母多一个
                    if(valid == len(t)):
                        validLen = right - left
                        validStart = left
                        if (validLen < minLen):
                            start = validStart
                            minLen = validLen

                while (valid == len(t)):
                    if(s[left] not in chardic.keys()):
                        left += 1
                        validStart = left
                        validLen -= 1
                        if (validLen < minLen):
                            start = validStart
                            minLen = validLen
                    elif(s[left] in chardic.keys()):
                        if (chardic[s[left]] > charValidList[s[left]]):
                            chardic[s[left]] -= 1
                            left += 1
                            validStart = left
                            validLen -= 1
                            if (validLen < minLen):
                                start = validStart
                                minLen = validLen
                        elif(chardic[s[left]] == charValidList[s[left]]):
                            chardic[s[left]] -= 1
                            valid -= charValidList[s[left]]
                            left += 1

            right += 1

        if (minLen>len(s)):
            return ""
        return s[start:(start + minLen+1)]





s = "ADOBECODEBANC"
t = "ABC"
mySolution = Solution()
print(mySolution.minWindow(s,t))