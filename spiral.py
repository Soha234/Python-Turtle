import turtle

sc = turtle.Screen()
sc.setup(400, 300)


pen = turtle.Turtle()
pen.pencolor("Green")


length = 1
angle = 90
increment = 5

for i in range(35):
    pen.forward(length)
    pen.right(angle)
    length += increment

turtle.done
