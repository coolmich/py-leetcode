from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        b, c, mapi = 0, 0, defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
            else:
                mapi[secret[i]] += 1
        for i in range(len(secret)):
            if secret[i] != guess[i] and mapi[guess[i]] > 0:
                c, mapi[guess[i]] = c + 1, mapi[guess[i]] - 1
        return '{}A{}B'.format(b, c)
