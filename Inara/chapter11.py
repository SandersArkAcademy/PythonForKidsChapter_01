import turtle
t = turtle.Pen()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
for x in range(1, 5):
    t.forward(50)
    t.left(90)

t.reset()
for x in range(1,9):
    t.forward(100)
    t.left(225)

t.reset()
for x in range(1, 38):
    t.forward(100)
    t.left(175)

t.reset()
for x in range(1,20):
    t.forward(100)
    t.left(95)

t.reset()
for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)

t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()

t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

t.color(1,1,0)
t.begin_fill()
t.circle(50)
t.end_fill()

def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

t.reset()

mycircle(0,1,0)
t.up()
t.forward(20)
t.down()
mycircle(0,0.5,0)
t.up()
t.left(90)
t.forward(20)
t.down()
mycircle(1,0,0)
t.up()
t.left(90)
t.forward(20)
t.down()
mycircle(0.5,0,0)
t.up()
t.left(90)
t.forward(20)
t.down()
mycircle(0,0,1)
t.up()
t.left(90)
t.forward(20)
t.down()
mycircle(0,0,0.5)
t.up()
t.left(90)
t.forward(30)
t.down()
mycircle(0.9,0.75,0)
t.up()
t.left(90)
t.forward(30)
t.down()
mycircle(1,0.7,0.75)
t.up()
t.left(90)
t.forward(30)
t.down()
mycircle(1,0.5,0)
t.up()
t.left(90)
t.forward(30)
t.down()
mycircle(0.9,0.5,0.15)

t.reset()
mycircle(0,0,0)

mycircle(1,1,1)

def mysquare(size):
    for x in range(1,5):
        t.forward(size)
        t.left(90)

t.color(0,0,0)

mysquare(50)

t.reset()
mysquare(25)
mysquare(50)
mysquare(75)
mysquare(100)
mysquare(125)

t.reset()
t.begin_fill()
mysquare(50)

t.end_fill()

def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()

t.reset()

mysquare(50, True)

mysquare(150, False)
t.reset()

for x in range(1,19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
t.reset()

def mystar(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()

t.color(0.9, 0.75, 0)
mystar(120, True)

t.color(0,0,0)
mystar(120, False)
t.reset()

for x in range(1, 9):
    t.forward(50)
    t.left(45)

def myoctagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()

t.color(0.9, 0.75, 0)
myoctagon(50, True)

t.color(0,0,0)
myoctagon(50, False)
t.reset()

def draw_star(size, points):
    angle = 360 / points
    for x in range(0, points):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.right(180-(angle * 2))

draw_star(50, 5)