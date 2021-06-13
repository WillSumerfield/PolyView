import tkinter as tk
import numpy as np
from polyview.graph import *

# region Window Creation

# Create the root window
root = tk.Tk()

# Stop Resizing
root.resizable(False, False)

# Rename the window's title
root.title("PolyView")

# endregion

# region Canvas Creation

graph_canvas = tk.Canvas(root, bg="white", height=512, width=512, highlightthickness=0)
graph_canvas.pack()
root.update()

# endregion

# region Test Dataset - 10 Houses, 3 Inputs, 1 Output Price
# [ [House Size (1-10)], [Mice Found (1-20)], [Bedrooms (1-5)], [House Price (1-50)] ]

# Inputs
house_size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mice_found = [15, 12, 14, 20, 0, 17, 2, 7, 5, 10]
bedrooms = [5, 2, 3, 1, 5, 4, 4, 3, 2, 1]

# Create Output
house_price = [0] * 10
for i in range(10):
    house_price[i] = (house_price[i]/10 + mice_found[i]/20 + bedrooms[i]/5) * (50 / 3)

# Create Test Array
test = np.array([house_size, mice_found, bedrooms, house_price])

# endregion

# region Graph Creation

test_graph = Graph("Test", house_size, graph_canvas)
test_graph.draw()

# endregion

# region Loop Window

root.mainloop()

# endregion
