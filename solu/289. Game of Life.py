class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def count_live(board, r, c):
            cnt = 0
            for r_ in range(max(0, r-1), min(len(board), r+2)):
                for c_ in range(max(0, c-1), min(len(board[0]), c+2)):
                    if r_ == r and c_ == c: continue
                    if board[r_][c_] == 1 or board[r_][c_] == -2: cnt += 1
            return cnt
        for r in range(len(board)):
            for c in range(len(board[0])):
                liveness = count_live(board, r, c)
                if board[r][c] and (liveness < 2 or liveness > 3):
                    board[r][c] = -2
                elif not board[r][c] and liveness == 3:
                    board[r][c] = 2
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 2: board[r][c] = 1
                elif board[r][c] == -2: board[r][c] = 0
