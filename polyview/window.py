import tkinter as tk
import numpy as np
from polyview.graph import *
import pandas as pd
from polyview.CONSTANTS import *

# region Window Creation

# Create the root window
root = tk.Tk()

# Stop Resizing
root.resizable(False, False)

# Rename the window's title
root.title("PolyView")

# endregion

# region Canvas Creation

graph_canvas = tk.Canvas(root, bg="white", height=WINDOW_WIDTH, width=WINDOW_HEIGHT, highlightthickness=0)
graph_canvas.pack()
root.update()

# endregion

# region Test Dataset - 10 Houses, 3 Inputs, 1 Output Price
# [ [House Size (1-10)], [Mice Found (1-20)], [Bedrooms (1-5)], [House Price (1-50)] ]

# Create Test Dataframe
test = pd.read_csv("../TestData.csv")

# endregion

# region Graph Creation

test_graph = Graph("Test", test, graph_canvas)
test_graph.draw()

# endregion

# region Loop Window

root.mainloop()

# endregion
