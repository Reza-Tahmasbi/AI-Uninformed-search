import turtle
def draw_maze(maze, path):
    # Define colors for the maze
    colors = {"#": "#191970", "-": "#483D8B", "%": "#000080", "S": "#8643B3", "G": "#4169E1"}

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Set the starting position
    x, y = -400, 300
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw the maze
    for row in maze:
        for cell in row:
            t.fillcolor(colors[cell])
            t.begin_fill()
            for _ in range(4):
                t.forward(60)
                t.right(90)
            t.end_fill()
            t.forward(60)
        t.backward(60 * len(row))
        t.right(90)
        t.forward(60)
        t.left(90)

    # Draw the path
    t.penup()
    x1, y1 = path[0] % len(maze[0]), path[0] // len(maze[0])
    t.goto(x + 30 + x1 * 60, y - 30 - y1 * 60)
    t.pendown()
    t.pencolor("white")
    t.pensize(5)

    # Show the turtle window
    for i in range(len(path) - 1):
        x1, y1 = path[i] % len(maze[0]), path[i] // len(maze[0])
        x2, y2 = path[i + 1] % len(maze[0]), path[i + 1] // len(maze[0])
        t.goto(x + 30 + x1 * 60, y - 30 - y1 * 60)
        t.goto(x + 30 + x2 * 60, y - 30 - y2 * 60)
        print(x1, y1, x2, y2)

    # Show the turtle window
    turtle.done()