import numpy as np
import tkinter as tk
import random
from polyview.dimension import *
from polyview.dimension_selector import *
import colour

class Graph:

    range_padding = 0.2

    def __init__(self, title, array, canvas, notch_count=10):

        # region Parameter Setting

        self.title = title
        self.array = array
        self.canvas = canvas
        self.notch_count = notch_count

        # endregion

        # region Constants

        # endregion

        # region Starting Variables

        # The starting rotation of this graph
        self.x_rotation = 0
        self.y_rotation = 0

        # Generate Colors
        starting_color = random.random()
        color_list = np.array(colour.Color(hue=1 % (starting_color + (i/10)), saturation=1, luminance=1) for i in range(10))

        # For every dimension, assign it a color
        self.Dimensions = np.array((dimension, color) for dimension, color in (array, color_list))

        # endregion

    def draw(self):
        dim = Dimension(self.canvas, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        dim.draw_horizontal()
        selector = DimensionSelector(self.canvas, self.Dimensions)
        selector.draw_horizontal()
