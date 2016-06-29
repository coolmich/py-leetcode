class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not len(board): return
        stack, j = [], 0
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                stack.append((0, i))
            if board[-1][i] == 'O':
                stack.append((len(board)-1, i))
        for i in range(len(board)):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][-1] == 'O':
                stack.append((i, len(board[0])-1))
        while j < len(stack):
            r, c = stack[j]
            j += 1
            if board[r][c] == '#': continue
            board[r][c] = '#'
            if r > 0 and board[r-1][c] == 'O':
                stack.append((r-1, c))
            if r < len(board) - 1 and board[r+1][c] == 'O':
                stack.append((r+1, c))
            if c > 0 and board[r][c-1] == 'O':
                stack.append((r, c-1))
            if c < len(board[0]) - 1 and board[r][c+1] == 'O':
                stack.append((r, c+1))
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
