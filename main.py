from draw_maze import draw_maze
from mazegraph import MazeGraph


def read_maze(file_name):
    file = open(file_name)  # read file
    lines = file.readlines()  # extract lines
    m, n = lines[0].split(',')  # get the grid size
    maze_map = []
    maze_map.extend([line.replace("\n","") for line in lines[1:]])  # store map
    n = str(n.replace("\n", ""))
    return int(m), int(n), maze_map


def find_start_goal(rows, cols):
    start_node = None
    goal_node = None
    # Find the starting and goal positions
    for i in range(rows):
        for j in range(cols):
            if maze_graph.maze[i][j] == "S":
                start_node = i * cols + j
            elif maze_graph.maze[i][j] == "G":
                goal_node = i * cols + j
    return start_node, goal_node


if __name__ == '__main__':
    file_name = "Test Case/test_case_1.txt"
    rows, cols, maze = read_maze(file_name)
    maze_graph = MazeGraph(rows, cols, maze)
    start_node, goal_node = find_start_goal(rows, cols)
    # Find the path from 'S' to 'G'
    path = maze_graph.bfs(start_node, goal_node)

    if path:
        print("Path from 'S' to 'G':", path)
        directions = maze_graph.get_directions(path)
        print("Directions:", directions)
        draw_maze(maze_graph.maze, path)
    else:
        print("No path found from 'S' to 'G'")
