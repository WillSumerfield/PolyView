""" Dimension class for the Graph class

A Dimension contains the information of a particular variable in the data set contained by the graph.
This includes both the data, and the graphical elements portrayed in the graph.
It has draw functions for both horizontal and vertical drawings, which draw the corresponding axis.

"""

import tkinter as tk
import numpy as np
from polyview.CONSTANTS import *


class Dimension:

    def __init__(self, canvas, array, color='black'):
        """ Construct a Dimension

        Parameter Types:

        CANVAS is a tkinter Canvas
        ARRAY is a Numpy Array
        COLOR is optional (defaults to white)

        Parameter Descriptions:

        CANVAS is the canvas to draw to
        ARRAY is the data to draw
        COLOR is the color theme drawn for this Dimension

        """

        # region Set Parameters

        self.canvas = canvas
        self.array = array
        self.color = color

        # endregion

        # region Variables

        self.min = min(array)
        self.max = max(array)

        # The range of the data
        self.range = self.max - self.min

        # endregion Variables

    def graph_x_to_real(self, x):
        return GRAPH_X + (((WINDOW_WIDTH - GRAPH_X)/self.range) * (x - self.min))

    def graph_y_to_real(self, y):
        return GRAPH_Y - ((GRAPH_Y/self.range) * (y - self.min))

    def get_notch_x(self, index):
        """ Get the x position of a horizontal notch

        Parameter Types:

        INDEX is an integer

        Parameter Descriptions:

        INDEX is the notch index

        """

        return HORIZONTAL_TEXT_STARTING_X + (index * HORIZONTAL_TEXT_NOTCH_SPACING)

    def get_notch_y(self, index):
        """ Get the y position of a vertical notch

        Parameter Types:

        INDEX is an integer

        Parameter Descriptions:

        INDEX is the notch index

        """
        return VERTICAL_BAR_Y + VERTICAL_BAR_HEIGHT - FRAME_SIZE - (index * VERTICAL_TEXT_NOTCH_SPACING)

    def draw_horizontal(self):
        """ Draw the Dimension horizontally

        This function is called by its graph to draw the dimension

        """

        # Draw Horizontal Bar
        self.canvas.create_polygon(
            HORIZONTAL_BAR_X,                        HORIZONTAL_BAR_Y,                          # Top Left
            HORIZONTAL_BAR_X + HORIZONTAL_BAR_WIDTH, HORIZONTAL_BAR_Y,                          # Top Right
            HORIZONTAL_BAR_X + HORIZONTAL_BAR_WIDTH, HORIZONTAL_BAR_Y + HORIZONTAL_BAR_HEIGHT,  # Bottom Right
            HORIZONTAL_BAR_X,                        HORIZONTAL_BAR_Y + HORIZONTAL_BAR_HEIGHT,  # Bottom Left
            fill=self.color                                                                     # Color
        )

        # Draw Notches and Numbers
        for i in range(NOTCHES):

            # Get Notch X
            notch_x = self.get_notch_x(i)

            # Draw Notch
            if (i != 0):
                self.canvas.create_line(
                    notch_x, HORIZONTAL_BAR_Y - NOTCH_LENGTH,   # Top, X adjusted for text width
                    notch_x, HORIZONTAL_BAR_Y,                  # Bottom
                    fill=self.color                             # Color
                )

            # Draw Number
            self.canvas.create_text(
                notch_x,                                  # X Position
                HORIZONTAL_TEXT_Y,                                          # Y Position
                text=str(round(self.min + ((i / NOTCHES) * self.range))),   # Text
                anchor=tk.N                                                # Cardinal Centering
            )

    def draw_vertical(self):
        """ Draw the Dimension Vertically

        This function is called by its graph to draw the dimension

        """

        # Draw Vertical Bar
        self.canvas.create_polygon(
            VERTICAL_BAR_X,                      VERTICAL_BAR_Y,                        # Top Left
            VERTICAL_BAR_X + VERTICAL_BAR_WIDTH, VERTICAL_BAR_Y,                        # Top Right
            VERTICAL_BAR_X + VERTICAL_BAR_WIDTH, VERTICAL_BAR_Y + VERTICAL_BAR_HEIGHT,  # Bottom Right
            VERTICAL_BAR_X,                      VERTICAL_BAR_Y + VERTICAL_BAR_HEIGHT,  # Bottom Left
            fill=self.color                                                             # Color
        )

        # Draw Notches and Numbers
        for i in range(NOTCHES):

            # Get Notch Y
            notch_y = self.get_notch_y(i)

            # Draw Notch
            if (i != 0):
                self.canvas.create_line(
                    VERTICAL_BAR_X + FRAME_SIZE,                notch_y,    # Top, Y adjusted for text height
                    VERTICAL_BAR_X + NOTCH_LENGTH + FRAME_SIZE, notch_y,    # Bottom, Y adjusted for text height
                    fill=self.color                                         # Color
                )

            # Draw Number
            self.canvas.create_text(
                VERTICAL_TEXT_X,                                            # X Position
                notch_y,                                 # Y Position
                text=str(round(self.min + ((i / NOTCHES) * self.range))),   # Text
                anchor=tk.E                                                # Cardinal Centering
            )