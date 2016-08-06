class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def extract_digit(word):
            i = 0
            while i < len(word) and word[i].isdigit(): i+=1
            return word[:i], word[i:]
        if not word: return ['']
        if len(word) == 1: return ['1', word]
        res = []
        for item in self.generateAbbreviations(word[1:]):
            res.append(word[0]+item)
            if item[0].isdigit():
                a, b = extract_digit(item)
                res.append(str(int(a)+1)+b)
            else: res.append('1'+item)
        return res
