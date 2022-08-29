class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        container = {}

        for i, num in enumerate(nums):
            if target - num in container:
                return [container[target - num], i]
            container[num] = i
        return


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
