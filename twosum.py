class Solution(object):
    def twoSum(self, nums, target):
        """"
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rlist = {} # val : index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in rlist:
                return [rlist[complement], i]
            rlist[n] = i
        return