import turtle
x = turtle.Turtle()

#Manual iteration
"""x.right(90)
x.forward(100)

x.left(90)
x.forward(100)

x.left(135)
x.forward(100*1.414)"""

for i in range(1,4):
  if (i == 3):
    x.left(135)
    x.forward(100*1.414)
  else:
    x.left(90)
    x.forward(100)
