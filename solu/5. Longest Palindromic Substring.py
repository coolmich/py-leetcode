class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        stri, maxi = '#' + '#'.join(list(s)) + '#', 0
        center, p = 0, [1]*len(stri)
        for i in range(len(stri)):
            p[i] = min(p[2*center-i], center+p[center]-i) if i < center+p[center] else 1
            while i-p[i] >= 0 and i+p[i] < len(stri) and stri[i-p[i]] == stri[i+p[i]]: p[i] += 1
            if i+p[i] > center + p[center]: center = i
            if p[i] > p[maxi]: maxi = i
        return ''.join(stri[maxi-p[maxi]+1:maxi+p[maxi]].split('#'))
print Solution().longestPalindrome("abb")