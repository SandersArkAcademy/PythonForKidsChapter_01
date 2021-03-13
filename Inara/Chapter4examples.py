import turtle

t = turtle.Pen()



longSide = 100
shortSide = 50

t.forward(shortSide)
t.right(90)
t.forward(longSide)
t.right(90)
t.forward(shortSide)
t.right(90)
t.forward(longSide)

for i in range(3):
     t.forward(longSide)
     t.right(120)
     t.left(20)
     t.backward(shortSide)

#      val = input("Hit enter for next example")

# for i in range(4):
#     t.up()
#     t.forward(shortSide)
#     t.down()
#     t.forward(longSide)
#     t.up()
#     t.forward(shortSide)
#     t.left(90)

turtle.done()