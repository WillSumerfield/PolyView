import numpy as np
import tkinter as tk
import random
from polyview.dimension import *
from polyview.dimension_selector import *
import colour


class Graph:

    range_padding = 0.2

    def __init__(self, title, dataframe, canvas, notch_count=10):

        # region Parameter Setting

        self.title = title
        self.dataframe = dataframe
        self.canvas = canvas
        self.notch_count = notch_count

        # endregion

        # region Starting Variables

        # Number of Columns
        columns = self.dataframe.columns.__len__()

        # The starting rotation of this graph
        self.x_rotation = 0
        self.y_rotation = 0

        # Randomly Create Colors
        starting_color = random.random()
        color_list = [None] * columns
        for i in range(columns):
            color_list[i] = colour.Color(hsl=((starting_color + (i/columns)) % 1, 1, 0.5))

        # For every dimension, assign it a color
        self.Dimensions = [(0, 0)] * columns
        for i in range(columns):
            self.Dimensions[i] = (self.dataframe.columns[i], color_list[i])

        # endregion

    def draw(self):
        dim = Dimension(self.canvas, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        dim.draw_horizontal()
        selector = DimensionSelector(self.canvas, self.Dimensions)
        selector.draw_horizontal()
