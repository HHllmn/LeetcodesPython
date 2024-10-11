class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_map = {}

        for i in range(len(nums)):
            if target - nums[i] in number_map:
                return [i, number_map[target - nums[i]]]
            number_map[nums[i]] = i
        
        return []
        