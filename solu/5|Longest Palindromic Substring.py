class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        start1, end1 = self.helper(s, 0)
        start2, end2 = self.helper(s, 1)
        start, end = (start1, end1) if end1-start1 > end2-start2 else (start2, end2)
        return s[start:end+1]

    def helper(self, s, even):
        start = end = 0
        for idx in range(len(s)):
            arm = 0
            ss, ee = idx-arm, idx+arm+even
            while ss >= 0 and ee < len(s):
                if s[ss] != s[ee]:
                    break
                if arm*2+1 > end-start:
                    start, end = ss, ee
                arm += 1
                ss, ee = idx-arm, idx+arm+even
        return start, end
