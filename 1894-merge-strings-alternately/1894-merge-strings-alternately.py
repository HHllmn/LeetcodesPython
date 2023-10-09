class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]
            
        return res + word1[i+1:] + word2[i+1:]