import turtle

t = turtle.Pen()

print("Make a square.")

t.forward(50)
t.right(90)     # Rotate clockwise by 90 degrees

t.forward(50)


t.right(90)

t.forward(50)
t.right(90)

t.forward(50)
t.right(90)


val = input("Hit enter for next example.")

t.clear()
t.setpos(0,0)

print("Make a square.")


# Loop 4 times. Everything I want to repeat is 
# *indented* by four spaces.
for i in range(4):
    t.forward(50)
    t.right(90)

val = input("Hit enter for next example.")

t.clear()
t.setpos(0,0)
print("Make a star.")


for i in range(5):
    t.forward(50)
    t.right(144)

val = input("Hit enter for next example.")

t.clear()
t.setpos(0,0)
print("Make a star 2.")

for i in range(78):
    t.forward(i * 10)
    t.right(144)

val = input("Hit enter for next example.")

t.clear()
t.setpos(0,0)
print("Make a star 2.")

t.clear()
t.setpos(0,0)
t.pencolor("blue")

for i in range(50):
    t.forward(50)
    t.left(123) # Let's go counterclockwise this time 
    
t.pencolor("red")
for i in range(50):
    t.forward(100)
    t.left(123)

turtle.done()

