from collections import deque

class Node:
    # initial function
    def __init__(self, pos, value):
        self.pos = pos
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
    m, n = int(grid_size[0]), int(grid_size[1])
    print(maze_map)
    g_pos = [(i, j) for i in range(m) for j in range(n) if
             maze_map[i][j] == 'G']
    s_pos = [(i, j) for i in range(m) for j in range(n) if
             maze_map[i][j] == 'S']
    return s_pos, g_pos


def bfs(s_pos, g_pos, maze_map, grid_size):
    grid_x, grid_y = int(grid_size[0]), int(grid_size[1])
    moves = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }
    starting_node = Node(s_pos, "S")
    queue = deque()
    moves_list = []
    queue.append(starting_node)

    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        if current_node.pos == g_pos:  # check if we reached the goal
            print(str(moves_list))
            return None

            # for i in range(4):
        visited_blocks = [[False for i in range(grid_x)]
                          for j in range(grid_y)]
        visited_blocks[int(s_pos[0])][int(s_pos[1])] = True
        x, y = int(current_node.pos[0]), int(current_node.pos[1])
        if not visited_blocks[x][y]:
            visited_blocks[x][y] = True
        x_pos = current_node.pos[0]
        y_pos = current_node.pos[1]
        top_edge_flag = False
        bottom_edge_flag = False

        for move in moves.values():
            new_x_pos = x_pos + move[0]
            new_y_pos = y_pos + move[1]
            if new_x_pos < grid_x and new_y_pos < grid_y and new_x_pos >= 0 and new_y_pos >= 0:
                if maze_map[new_x_pos][new_y_pos] == 1:
                    if not visited_blocks[new_x_pos][new_y_pos]:
                        new_node = Node((new_y_pos, new_y_pos),
                                        maze_map[new_x_pos][new_y_pos])
                        visited_blocks[new_x_pos][new_y_pos] = True
                        queue.append(new_node)


if __name__ == '__main__':
    grid_size, maze_map = read_maze()
    s_pos, g_pos = find_S_G(grid_size, maze_map)
