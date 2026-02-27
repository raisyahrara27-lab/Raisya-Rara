import turtle

def draw_spiral(t, steps, length):
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    for i in range(steps):
        t.pencolor(colors[i % 6])
        t.forward(i * length / steps)
        t.left(59) # Sudut sedikit kurang dari 60 untuk efek spiral

# Setup
pen = turtle.Turtle()
pen.speed(0)
turtle.bgcolor("black")

draw_spiral(pen, 200, 500)
turtle.done()