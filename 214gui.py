import tkinter as tk
# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

blue = tk.Canvas(height = 100, width = 130, background = "blue")
blue.grid(row = 0, column = 0)

green = tk.Canvas(height = 100, width = 60.5, background = "green")
green.grid(row = 0, column = 130)

yellow = tk.Canvas(height = 100, width = 60.5, background = "yellow")
yellow.grid(row = 100, column = 130)

red = tk.Canvas(height = 100, width = 130, background = "red")
red.grid(row = 100, column = 0)

root.mainloop()