class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        num = 0
        for char in t:
            if num == len(s): return True
            elif (s[num] == char): num += 1
        
        return num == len(s)
        