from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width=1200, height=1000)
canvas.pack()
my_image = PhotoImage(file="C:\\Users\\inara\\Desktop\\test.gif")
canvas.create_image(0, 0, anchor=NW, image=my_image)

for x in range(0, 120):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)


tk.mainloop()