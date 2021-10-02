class Solution(object):
    def getConcatenation(self, nums):
        ans = []

        for i in range(0, len(nums) * 2):
            ans = nums * 2
        return ans