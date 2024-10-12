class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alphabet = [0] * 26
        for char in s:
            alphabet[ord(char)-ord('a')] += 1
        for char in t:
            alphabet[ord(char)-ord('a')] -= 1
        for i in alphabet:
            if i != 0:
                return False
        return True
    