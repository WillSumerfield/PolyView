""" Dimension class for the Graph class

A Dimension contains the information of a particular variable in the data set contained by the graph.
This includes both the data, and the graphical elements portrayed in the graph.
It has draw functions for both horizontal and vertical drawings, which draw the corresponding axis.

"""

import tkinter as tk
import numpy as np
from polyview.CONSTANTS import *


class Dimension:

    def __init__(self, canvas, array, notches, color='black'):
        """ Construct a Dimension

        Parameter Types:

        CANVAS is a tkinter Canvas
        ARRAY is a Numpy Array
        NOTCHES is an integer
        COLOR is optional (defaults to white)

        Parameter Descriptions:

        CANVAS is the canvas to draw to
        ARRAY is the data to draw
        NOTCHES is the number of number-labels along the axis
        COLOR is the color theme drawn for this Dimension

        """

        # region Set Parameters

        self.canvas = canvas
        self.array = array
        self.notches = notches
        self.color = color

        # endregion

        # region Constants

        # region Horizontal

        self.HORIZONTAL_BAR_X = DIMENSION_SELECTOR_SPACING
        self.HORIZONTAL_BAR_Y = canvas.winfo_height() - DIMENSION_SELECTOR_SPACING

        self.HORIZONTAL_BAR_WIDTH = canvas.winfo_width() - self.HORIZONTAL_BAR_X
        self.HORIZONTAL_BAR_HEIGHT = 2

        self.HORIZONTAL_TEXT_STARTING_X = self.HORIZONTAL_BAR_X
        self.HORIZONTAL_TEXT_Y = self.HORIZONTAL_BAR_Y + 8
        self.HORIZONTAL_TEXT_NOTCH_SPACING = self.HORIZONTAL_BAR_WIDTH / self.notches

        # endregion

        # endregion

    def draw_horizontal(self):
        """ Draw the Dimension Horizontally

        This function is called by its graph to draw the dimension

        """

        # Draw Horizontal Bar
        self.canvas.create_polygon(
            self.HORIZONTAL_BAR_X,                             self.HORIZONTAL_BAR_Y,                               # Top Left
            self.HORIZONTAL_BAR_X + self.HORIZONTAL_BAR_WIDTH, self.HORIZONTAL_BAR_Y,                               # Top Right
            self.HORIZONTAL_BAR_X + self.HORIZONTAL_BAR_WIDTH, self.HORIZONTAL_BAR_Y + self.HORIZONTAL_BAR_HEIGHT,  # Bottom Right
            self.HORIZONTAL_BAR_X,                             self.HORIZONTAL_BAR_Y + self.HORIZONTAL_BAR_HEIGHT,  # Bottom Left
            fill=self.color                                                                                         # Color
        )

        # Draw Notches
        for i in range(self.notches):

            # Get Notch X
            notch_x = self.HORIZONTAL_BAR_X + (i * self.HORIZONTAL_TEXT_NOTCH_SPACING)

            # Draw Notch
            self.canvas.create_line(
                notch_x + 2, self.HORIZONTAL_BAR_Y - 2,    # Top, X adjusted for text width
                notch_x + 2, self.HORIZONTAL_BAR_Y,        # Bottom
                fill=self.color                             # Color
            )

            # Draw Number
            self.canvas.create_text(
                notch_x,                    # X Position
                self.HORIZONTAL_TEXT_Y,     # Y Position
                text=str(i),                # Text
                anchor=tk.W                 # Cardinal Centering
            )
