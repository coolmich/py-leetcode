class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        lengs = ','.join([str(len(stri)) for stri in strs])
        return str(len(strs)) + '|' + str(len(lengs)) + '|' + lengs + ''.join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i, firstI, secI = 0, 0, 0
        while i < len(s):
            if s[i] == '|':
                if not firstI: firstI = i
                elif not secI: secI = i
                else: break
            i += 1
        if not int(s[:firstI]): return []
        len_of_lengs = int(s[firstI+1:secI])
        lengs, reals = s[secI+1:secI+len_of_lengs+1].split(',')[::-1], s[secI+len_of_lengs+1:]
        cur, res = 0, []
        while lengs:
            length = int(lengs.pop())
            res.append(reals[cur:cur+length])
            cur += length
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))