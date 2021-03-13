import turtle

t = turtle.Pen()

print ("Make a square.")

t.forward(50)
t.right(90)

t.forward(50)


t.right(90)

t.forward(50)
t.right(90)

t.forward(50)
t.right(90)


val = input("Hit enter for next example")
t.clear()
t.reset()

print("Make a square")


for i in range(4):
    t.forward(50)
    t.right(90)

val = input