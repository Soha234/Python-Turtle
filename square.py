import turtle

turtle.Screen().bgcolor("Mistyrose")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome To Turtle Window")

pen = turtle.Turtle()

for i in range (4):
    
    pen.forward(100)
    pen.left(90)

turtle.done