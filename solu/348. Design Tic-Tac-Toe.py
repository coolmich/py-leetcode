class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[0 for i in range(n)] for j in range(n)]


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        def check_rc(r, c, grid):
            c1 = c2 = True
            c3 = c4 = False
            for i in range(len(grid)):
                if grid[i][c] != grid[r][c]: c1 = False
                if grid[r][i] != grid[r][c]: c2 = False
            if r == c:
                for i in range(len(grid)):
                    if grid[i][i] != grid[r][c]: c4 = True
                if not c4: c3 = True
            c4 = False
            if r+c == len(grid)-1:
                for i in range(len(grid)):
                    if grid[i][len(grid)-1-i] != grid[r][c]: c4 = True
                if not c4: c3 = True
            return c1 or c2 or c3

        self.grid[row][col] = player
        return player if check_rc(row, col, self.grid) else 0


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
# ["TicTacToe","move","move","move","move","move","move"]
arr = [[1,2,2],[0,2,1],[0,0,2],[2,0,1],[0,1,2],[1,1,1]]
for mv in arr:
    print obj.move(*mv)