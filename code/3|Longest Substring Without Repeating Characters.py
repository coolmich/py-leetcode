class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        mapi = {}
        # norep_start: the start of a non repetition region
        longest_len = norep_start = 0
        for idx, letter in enumerate(s):
            if letter in mapi and mapi[letter] >= norep_start:
                norep_start = mapi[letter] + 1
            mapi[letter] = idx
            longest_len = max(longest_len, idx - norep_start + 1)
        return longest_len
