class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 1
        while (i < len(nums)):
            while (j < len(nums)):
                print(nums[i])
                print(nums[j])
                j += 1
            i += 1


