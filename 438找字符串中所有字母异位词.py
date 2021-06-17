class Solution(object):
    def findAnagrams(self, s, t):

        chardic = {}
        for char in list(t):
            chardic[char] = 0
        charValidList = chardic.copy()
        for char in list(t):
            charValidList[char] += 1
        left = 0
        right = 0

        minLen = len(s) + 1
        valid = 0
        allleft = []
        validLen = len(s) + 1
        while (right < len(s)):

            if (s[right] in chardic.keys()):
                chardic[s[right]] += 1
                if (chardic[s[right]] == charValidList[s[right]]):  # 窗口中第一个符合的
                    valid += charValidList[s[right]]  # 符合条件的字母多一个
                    if (valid == len(t)):
                        validLen = right - left + 1

                while (valid == len(t)):
                    if (validLen == len(t)): all.append(left)
                    if (s[left] not in chardic.keys()):
                        left += 1
                        validLen -= 1

                    elif (s[left] in chardic.keys()):
                        if (chardic[s[left]] > charValidList[s[left]]):
                            chardic[s[left]] -= 1
                            left += 1
                            validLen -= 1

                        elif (chardic[s[left]] == charValidList[s[left]]):
                            chardic[s[left]] -= 1
                            valid -= charValidList[s[left]]
                            left += 1

            right += 1
        if(len()>0):
            return allleft
        return False
