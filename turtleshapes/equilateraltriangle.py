import turtle
x = turtle.Turtle()

#Manual code iteration
"""x.right(120)
x.forward(100)
x.right(120)
x.forward(100)
x.right(120)
x.forward(100)"""


x.fillcolor("#09d68e")

x.begin_fill()
for i in range(1,4):
  x.right(120)
  x.forward(100)
x.end_fill()




