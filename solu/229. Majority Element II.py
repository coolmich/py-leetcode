from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        const_map, final = {}, defaultdict(int)
        for num in nums:
            if num in const_map:
                const_map[num] = const_map[num] + 1 if num in const_map else 1
            else:
                if len(const_map) < 2:
                    const_map[num] = 1
                else:
                    to_delete = []
                    for k in const_map:
                        const_map[k] -= 1
                        if not const_map[k]: to_delete.append(k)
                    for k in to_delete: const_map.pop(k, None)
        for num in nums:
            if num in const_map: final[num] += 1
        return [k for k in final if final[k] > len(nums)/3]