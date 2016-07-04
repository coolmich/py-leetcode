class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the complexity comes from maintaining constant space
        const_map = {}
        for num in nums:
            if num in const_map:
                const_map[num] += 1
            else:
                if len(const_map) < 2:
                    const_map[num] = 1
                else:
                    rm = []
                    for k in const_map:
                        const_map[k] -= 1
                        if not const_map[k]: rm.append(k)
                    for item in rm:
                        const_map.pop(item, None)
        if len(const_map) == 1:
            return const_map.keys()[0]
        else:
            ks = const_map.keys()
            return ks[0] if const_map[ks[0]] > const_map[ks[1]] else ks[1]