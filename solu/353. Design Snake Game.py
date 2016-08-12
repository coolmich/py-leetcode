from collections import deque
class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.q = deque([(0,0)])
        self.food = food[::-1]
        self.w = width
        self.h = height

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        r, c = self.q[-1]
        if direction == 'U':
            nr, nc = r-1, c
        elif direction == 'L':
            nr, nc = r, c-1
        elif direction == 'R':
            nr, nc = r, c+1
        else:
            nr, nc = r+1, c
        if self.food and [nr, nc] == self.food[-1]:
            self.food.pop()
        else:
            self.q.popleft()
        if nr < 0 or nr >= self.h or nc < 0 or nc >= self.w or (nr, nc) in self.q: return -1
        self.q.append((nr, nc))
        return len(self.q) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)