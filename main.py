from collections import deque

class Node:
    # initial function
    def __init__(self, pos, value, parent=None):
        self.pos = pos # the position of node
        self.value = value # the value of node
        self.parent = parent # parent of each node, root parent is None


# read the file
def read_maze():
    file = open("Test Case/test_case_2.txt") # read file
    lines = file.readlines() # exract lines
    m, n = lines[0].split(',') # get the grid size
    map = []
    map.extend([[char for char in line.strip()] for line in lines[1:]]) # store map
    return (m, n), map


# find start and goal node
def find_S_G(grid_size, maze_map):
    m, n = int(grid_size[0]), int(grid_size[1])
    print(maze_map)
    goal_pos = [(i, j) for i in range(m) for j in range(n) if
             maze_map[i][j] == 'G'][0]
    start_pos = [(i, j) for i in range(m) for j in range(n) if
             maze_map[i][j] == 'S'][0]
    return start_pos, goal_pos


# bfs algorithm
def bfs(start_pos, goal_pos, maze_map, grid_size):
    grid_x, grid_y = int(grid_size[0]), int(grid_size[1]) # extract size of the grid
    moves = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0),
    }
    node = Node(start_pos, "S")
    queue = deque()
    stored_moves = []
    queue.append(node)
    for item in queue:
        print(item.value)
    visited_blocks = [[False for i in range(grid_x)]
                      for j in range(grid_y)]
    visited_blocks[int(start_pos[0])][int(start_pos[1])] = True

    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        print(current_node.pos, goal_pos)
        if current_node.pos == goal_pos:  # check if we reached the goal
            while current_node.parent is not None:
                # print(current_node.parent.pos)
                dx, dy = current_node.pos[0] - current_node.parent.pos[0], current_node.pos[1] - current_node.parent.pos[1]
                if (dx, dy) == moves['R']:
                    stored_moves.append('R')
                elif (dx, dy) == moves['L']:
                    stored_moves.append('L')
                elif (dx, dy) == moves['U']:
                    stored_moves.append('U')
                elif (dx, dy) == moves['D']:
                    stored_moves.append('D')
                current_node = current_node.parent
            return stored_moves[::-1]

        # x, y = int(current_node.pos[0]), int(current_node.pos[1])
        # if not visited_blocks[x][y]:
        #     visited_blocks[x][y] = True
        x_pos = current_node.pos[0]
        y_pos = current_node.pos[1]
        for move in moves.values():
            new_x_pos = x_pos + move[0]
            new_y_pos = y_pos + move[1]
            # print(new_x_pos, new_y_pos)
            if grid_x > new_x_pos >= 0 and grid_y > new_y_pos >= 0:
                print(new_x_pos, new_y_pos, len(visited_blocks), len(visited_blocks[0]))
                if maze_map[new_x_pos][new_y_pos] == "-" or maze_map[new_x_pos][new_y_pos] == "G":
                    if not visited_blocks[new_x_pos][new_y_pos]:
                        node = Node((new_x_pos, new_y_pos),
                                    maze_map[new_x_pos][new_y_pos], node)
                        visited_blocks[new_x_pos][new_y_pos] = True
                        queue.append(node)
                        print(node.value)

if __name__ == '__main__':
    grid_size, maze_map = read_maze()
    s_pos, g_pos = find_S_G(grid_size, maze_map)
    moves_list = bfs(s_pos, g_pos, maze_map, grid_size)
    print(''.join(moves_list))