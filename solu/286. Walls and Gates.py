class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        stack = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if not rooms[r][c]: stack.append((r, c))
        while stack:
            row, col = stack.pop()
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row+x, col+y
                if 0 <= r < len(rooms) and 0 <= c < len(rooms[0]) and rooms[r][c] > rooms[row][col]+1:
                    rooms[r][c] = rooms[row][col]+1
                    stack.append((r, c))
        