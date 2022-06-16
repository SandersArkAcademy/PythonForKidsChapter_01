import turtle
t= turtle.Pen()
print ("Make a square.")

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

val = input("Hit enter for next example")

t.reset()
print("Make two lines")

t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)

val = input("Hit enter for next example")

print("Make a rectangle")
t.reset()

t.forward(50)
t.left(90)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)


val = input("Hit enter for next example")

print("Make a triangle")
t.reset()

t.right(45)
t.forward(73)
t.right(135)
t.forward(105)
t.right(135)
t.forward(75)

val = input("Hit enter for next example")

print("Make a box without corners")
t.reset()

t.forward(60)
t.up()
t.forward(20)
t.right(90)
t.forward(20)
t.down()
t.forward(60)
t.up()
t.forward(20)
t.right(90)
t.forward(20)
t.down()
t.forward(60)
t.up()
t.forward(20)
t.right(90)
t.forward(20)
t.down()
t.forward(60)

val = input("Hit enter to end program")