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

    def draw_horizontal(self):
        """ Draw the Dimension Horizontally

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
            notch_x = HORIZONTAL_TEXT_STARTING_X + (i * HORIZONTAL_TEXT_NOTCH_SPACING)

            # Draw Notch
            self.canvas.create_line(
                notch_x, HORIZONTAL_BAR_Y - NOTCH_LENGTH,   # Top, X adjusted for text width
                notch_x, HORIZONTAL_BAR_Y,                  # Bottom
                fill=self.color                             # Color
            )

            # Draw Number
            self.canvas.create_text(
                notch_x - TEXT_HALF_WIDTH,  # X Position
                HORIZONTAL_TEXT_Y,          # Y Position
                text=str(i),                # Text
                anchor=tk.NW                # Cardinal Centering
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
            notch_y = VERTICAL_BAR_Y + VERTICAL_BAR_HEIGHT - FRAME_SIZE - (i * VERTICAL_TEXT_NOTCH_SPACING)

            # Draw Notch
            self.canvas.create_line(
                VERTICAL_BAR_X + FRAME_SIZE,                notch_y,    # Top, Y adjusted for text height
                VERTICAL_BAR_X + NOTCH_LENGTH + FRAME_SIZE, notch_y,    # Bottom, Y adjusted for text height
                fill=self.color                                         # Color
            )

            # Draw Number
            self.canvas.create_text(
                VERTICAL_TEXT_X,                # X Position
                notch_y - TEXT_HALF_HEIGHT,     # Y Position
                text=str(i),                    # Text
                anchor=tk.NW                    # Cardinal Centering
            )