class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        li = []
        if numRows == 1: return s
        for k in range(numRows):
            i = k
            while i < len(s):
                li.append(s[i])
                if k != 0 and k != numRows-1:
                    j = i + (numRows-k-1)*2
                    if j < len(s):
                        li.append(s[j])
                i += (numRows-1)*2
        return "".join(li)