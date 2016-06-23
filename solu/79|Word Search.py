class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not self.precheck(board, word): return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                boardPos = (r, c)
                if self.helper(board, word, 0, (r, c)):
                    return True
        return False

    def precheck(self, board, word):
        dic = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                dic[board[r][c]] = 1 if board[r][c] not in dic else dic[board[r][c]]+1
        for l in word:
            if l not in dic: return False
            dic[l] -= 1
            if dic[l] < 0: return False
        return True

    def helper(self, board, word, idxNow, boardPos):
        if idxNow == len(word): return True
        if word[idxNow] == board[boardPos[0]][boardPos[1]]:
            board[boardPos[0]][boardPos[1]] = None
            for r, c in self.validPos(board, boardPos):
                if self.helper(board, word, idxNow+1, (r, c)):
                    return True
            board[boardPos[0]][boardPos[1]] = word[idxNow]
            return False
        else:
            return False

    def validPos(self, board, boardPos):
        valid = []
        r, c = boardPos
        w, h = len(board[0]), len(board)
        if r > 0 and board[r-1][c]: valid.append((r-1, c))
        if r < h-1 and board[r+1][c]: valid.append((r+1, c))
        if c > 0 and board[r][c-1]: valid.append((r, c-1))
        if c < w-1 and board[r][c+1]: valid.append((r, c+1))
        return valid
        