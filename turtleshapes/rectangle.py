import turtle
x = turtle.Turtle()

""""
x.forward(100)
x.right(90)

x.forward(50)
x.right(90)

x.forward(100)
x.right(90)

x.forward(50)
x.right(90)
"""

for i in range(1,5):
 if (i%2 == 0):
   x.forward(50)
   x.right(90)
 else:
   x.forward(100)
   x.right(90)
   
