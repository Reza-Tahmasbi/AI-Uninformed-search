from collections import deque
class MazeGraph:
    def __init__(self, rows, cols, maze):
        self.rows = rows
        self.cols = cols
        self.maze = [row.replace(" ", "") for row in maze]
        self.adj = self.create_adjacency_matrix()

    def create_adjacency_matrix(self):
        adj = [[0 for _ in range(self.rows * self.cols)] for _ in
               range(self.rows * self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] != '%':
                    current_node = i * self.cols + j
                    # Check and add neighbors (up, down, left, right)
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1),
                                 (i, j + 1)]:
                        if 0 <= x < self.rows and 0 <= y < self.cols and \
                                self.maze[x][y] != '%':
                            neighbor_node = x * self.cols + y
                            adj[current_node][neighbor_node] = 1
        return adj

    def bfs(self, start, goal):
        visited = [False] * (self.rows * self.cols)
        parent = [-1] * (self.rows * self.cols)
        queue = deque([start])
        visited[start] = True
        while queue:
            current_node = queue.popleft()
            for neighbor in range(self.rows * self.cols):
                if self.adj[current_node][neighbor] == 1 and not visited[
                    neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current_node
                    if neighbor == goal:
                        return self.construct_path(parent, start, goal)
        return None  # No path found

    def construct_path(self, parent, start, goal):
        path = []
        current_node = goal
        while current_node != -1:
            path.append(current_node)
            current_node = parent[current_node]
        return path[::-1]

    def get_directions(self, path):
        directions = []
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            current_i, current_j = divmod(current_node, self.cols)
            next_i, next_j = divmod(next_node, self.cols)
            if current_i < next_i:
                directions.append("D")
            elif current_i > next_i:
                directions.append("U")
            elif current_j < next_j:
                directions.append("R")
            elif current_j > next_j:
                directions.append("L")
        return directions