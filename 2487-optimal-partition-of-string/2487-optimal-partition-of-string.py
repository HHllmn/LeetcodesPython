class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """

        substrings = []
        current = []

        for char in s:
            if char in current:
                substrings.append(''.join(current))
                current[:] = []

            current.append(char)
        
        substrings.append(''.join(current))
        
        return len(substrings)

        