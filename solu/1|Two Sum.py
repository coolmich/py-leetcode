class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        mapi = {}
        index = 0
        for num in nums:
            if num in mapi:
                return [mapi[num], index]
            mapi[target-num] = index
            index += 1
        return None