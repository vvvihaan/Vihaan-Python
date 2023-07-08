import turtle
x = turtle.Turtle()

for j in range(10, 51, 10): #square repeatation
  for i in range(0,4): #creates squares
    x.forward(j)
    x.right(90)