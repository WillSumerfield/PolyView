import numpy as np
import tkinter as tk
import random
from polyview.dimension import *
from polyview.dimension_selector import *
import colour


class Graph:

    def __init__(self, title, dataframe, canvas, notch_count=10):

        # region Parameter Setting

        self.title = title
        self.dataframe = dataframe.dropna()
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
            self.dimensions[i] = (self.dataframe[self.dataframe.columns[i]], color_list[i])

        # Create a starting horizontal and vertical dimensions
        self.horizontal_dimension = Dimension(self.canvas, self.dimensions[0][0], self.dimensions[0][1])
        self.vertical_dimension = Dimension(self.canvas, self.dimensions[1][0], self.dimensions[1][1])

        # Create a Dimension Selector
        #self.horizontal_selector = DimensionSelector(self.canvas, self.dimensions)

        # endregion

    def draw_grid(self):

        # Draw Horizontal Lines
        for i in range(NOTCHES):
            self.canvas.create_line(
                GRAPH_X,
                self.horizontal_dimension.get_notch_y(i),
                WINDOW_WIDTH,
                self.horizontal_dimension.get_notch_y(i),
                fill=GRID_COLOR
            )

        # Draw Vertical Lines
        for i in range(NOTCHES):
            self.canvas.create_line(
                self.horizontal_dimension.get_notch_x(i),
                0,
                self.horizontal_dimension.get_notch_x(i),
                GRAPH_Y,
                fill=GRID_COLOR
            )

    def draw(self):

        # Draw Grid
        self.draw_grid()

        # Draw Dimensions
        self.horizontal_dimension.draw_horizontal()
        self.vertical_dimension.draw_vertical()

        # Draw Points
        for i in range(max(self.horizontal_dimension.array.__len__(), self.vertical_dimension.array.__len__())):

            # Get the real points
            real_x = round(self.horizontal_dimension.graph_x_to_real(self.horizontal_dimension.array[i]))
            real_y = round(self.vertical_dimension.graph_y_to_real(self.vertical_dimension.array[i]))

            # Draw the Point
            self.canvas.create_polygon(
                real_x - (POINT_SIZE-1), real_y + POINT_SIZE,
                real_x - (POINT_SIZE-1), real_y - (POINT_SIZE-1),
                real_x + POINT_SIZE,     real_y - (POINT_SIZE-1),
                real_x + POINT_SIZE,     real_y + POINT_SIZE,
                fill=POINT_COLOR
            )

        #self.selector.draw_horizontal()
