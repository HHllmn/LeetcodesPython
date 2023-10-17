class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for char in t:
            if s == "": return True
            elif (s[0] == char): s = s[1:]
        
        if s == "": return True
        else: return False
        