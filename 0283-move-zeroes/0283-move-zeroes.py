class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """      
        z = 0
        for i in xrange(len(nums)):
            if (nums[i] != 0):
                nums[i], nums[z] = nums[z],nums[i]
                z += 1
        

