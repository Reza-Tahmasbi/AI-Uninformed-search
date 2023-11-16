class Node:
    # initial function
    def __init__(self, x_pos, y_pos, value):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value


# read the whole Maze
def read_maze():
    file = open("Maze_env.txt")
    lines = file.readlines()
    # get the grid size
    m, n = lines[0].split(',')
    # read the map
    maze_map = []
    maze_map.extend([[char for char in line.strip()] for line in lines[1:]])
    return (m, n), maze_map


# find the start and the goal
def find_S_G(grid_size, maze_map):
    m,n = grid_size
    m, n = int(m), int(n)
    print(maze_map)
    g_pos = [(i, j) for i in range(m) for j in range(n) if
                        maze_map[i][j] == 'G']
    s_pos = [(i, j) for i in range(m) for j in range(n) if
                        maze_map[i][j] == 'S']
    return s_pos, g_pos

def bfs(s_pos, g_pos, maze_map):



if __name__ == '__main__':
    grid_size, maze_map = read_maze()
    s_pos, g_pos = find_S_G(grid_size, maze_map)