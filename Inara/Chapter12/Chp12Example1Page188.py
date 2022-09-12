from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.move(1, 5, 0)
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')
canvas.move(mytriangle, 5, 0)

canvas.itemconfig(mytriangle, fill='blue')

canvas.itemconfig(mytriangle, outline='red')

tk.mainloop()