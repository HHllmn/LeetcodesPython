class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        zeroes = 1
        res = 0
        for f in flowerbed:
            if f == 0:
                zeroes += 1
            else:
                res += (zeroes - 1) // 2
                zeroes = 0
        return res + (zeroes // 2) >= n