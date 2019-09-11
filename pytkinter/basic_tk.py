import tkinter as tk

height = 700
width = 800

top = tk.Tk()

canvas = tk.Canvas(top, height=height, width=width)
canvas.pack()

frame = tk.Frame(top)
frame.place(relwidth=0.1, relheight=0.1)

button = tk.Button(top, text="clicky", bg="gray")
button.pack()

top.mainloop()

