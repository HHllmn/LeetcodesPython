class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 1
        current = set()

        for char in s:
            if char in current:
                count += 1
                current.clear()

            current.add(char)
        
        return count

        