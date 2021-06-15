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
            color_list[i] = colour.Color(hsl=((starting_color + (i/columns)) % 1, 1, 0.4))

        # For every dimension, assign it a color
        self.dimensions = [(0, 0)] * columns
        for i in range(columns):
            self.dimensions[i] = (self.dataframe.columns[i], color_list[i])

        # Create a Dimension Selector
        #self.horizontal_selector = DimensionSelector(self.canvas, self.dimensions)

        # Create a starting horizontal dimension
        self.horizontal_dimension = Dimension(self.canvas, self.dimensions[0][0], self.dimensions[0][1])
        self.vertical_dimension = Dimension(self.canvas, self.dimensions[1][0], self.dimensions[1][1])

        # endregion

    def draw_grid(self):
        # Draw Horizontal Lines
        for i in range(NOTCHES):
            self.canvas.create_line(
                GRAPH_X,
                self.horizontal_dimension.get_notch_y(i),
                WINDOW_WIDTH,
                self.horizontal_dimension.get_notch_y(i)
            )

        # Draw Vertical Lines
        for i in range(NOTCHES):
            self.canvas.create_line(
                self.horizontal_dimension.get_notch_x(i),
                0,
                self.horizontal_dimension.get_notch_x(i),
                GRAPH_Y
            )

    def draw(self):
        self.draw_grid()
        self.horizontal_dimension.draw_horizontal()
        self.vertical_dimension.draw_vertical()
        #self.selector.draw_horizontal()
