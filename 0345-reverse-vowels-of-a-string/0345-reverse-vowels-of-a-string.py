class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        chars = list(s)
        start = 0
        end = len(s) - 1

        while (start < end):
            while (start < end) and (chars[start] not in vowels):
                start += 1
            while (start < end) and (chars[end] not in vowels):
                end -= 1

            chars[start], chars[end] = chars[end], chars[start]
            start +=1
            end -= 1
        
        return "".join(chars)