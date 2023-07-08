import turtle
x = turtle.Turtle()

"""x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.forward(100)"""

x.fillcolor("red") #setting the color to the turtle

x.begin_fill() #marking the start point of the shape to fill color

for i in range(0,4):
  x.forward(100)
  x.right(90)
  
x.end_fill() # marking the end point of the shape and start filling the color
  
  