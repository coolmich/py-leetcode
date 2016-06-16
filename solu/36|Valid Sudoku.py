class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols, blocks = {}, {}, {}
        for r in range(len(board)):
            for c in range(len(board[r])):
                num = board[r][c]
                if num == '.': continue
                if not self.helper(rows, r, num) or not self.helper(cols, c, num) or not self.helper(blocks, (r/3, c/3), num):
                    return False
        return True

    def helper(self, mapi, key, val):
        ss = mapi[key] if key in mapi else set([])
        if val in ss:
            return False
        else:
            ss.add(val)
            mapi[key] = ss
            return True
