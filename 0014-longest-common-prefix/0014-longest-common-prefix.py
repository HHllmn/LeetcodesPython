class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = min(strs)
        
        char = ''
        current = ""
        for i in range(len(length)):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return current
            current += char

        return current
        