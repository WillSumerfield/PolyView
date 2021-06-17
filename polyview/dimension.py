""" Dimension class for the Graph class

A Dimension contains the information of a particular variable in the data set contained by the graph.
This includes both the data, and the graphical elements portrayed in the graph.
It has draw functions for both horizontal and vertical drawings, which draw the corresponding axis.

"""

import tkinter as tk
import numpy as np
from polyview.CONSTANTS import *
import math


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

        # The min and max points in the array
        self.point_min = min(array)
        self.point_max = max(array)

        # The range of the data
        self.point_range = self.point_max - self.point_min

        # The min and max values the graph shows
        self.graph_min = self.point_min - (GRID_PADDING * self.point_range)
        self.graph_max = self.point_max + (GRID_PADDING * self.point_range)

        # The range of values the graph can show
        self.graph_range = self.graph_max - self.graph_min

        # The significant figures to display the notch text to
        self.sigfigs = max(-math.ceil(math.log(self.point_range, 10)) + 3, 0)

        # endregion Variables

    def get_number(self, index):
        """ Return the number at the given index as a string.
        The number will have sigfigs proportional to the range of the data.

        Parameter Types:

        INDEX is an integer

        Parameter Descriptions:

        INDEX is the notch index

        """

        # Get number to draw
        num = self.point_min + ((index / (NOTCHES-1)) * self.point_range)

        # Round the number to the correct number of digits
        num = round(num, self.sigfigs)

        # Set the number to a string with the correct number of digits
        string = ('{0:.' + str(self.sigfigs) + 'f}').format(num)

        return string

    def graph_x_to_real(self, x):
        """ Get the real x position from a graph position

        Parameter Types:

        X is a number

        Parameter Descriptions:

        X is the graph position from which to get the real position

        """

        return GRAPH_X + (((WINDOW_WIDTH - GRAPH_X)/self.graph_range) * (x - self.graph_min))

    def graph_y_to_real(self, y):
        """ Get the real y position from a graph position

        Parameter Types:

        Y is a number

        Parameter Descriptions:

        Y is the graph position from which to get the real position

        """

        return GRAPH_Y - ((GRAPH_Y/self.graph_range) * (y - self.graph_min))

    def get_notch_x(self, index):
        """ Get the x position of a horizontal notch

        Parameter Types:

        INDEX is an integer

        Parameter Descriptions:

        INDEX is the notch index

        """

        return self.graph_x_to_real(self.point_min + (index * (self.point_range/(NOTCHES-1))))

    def get_notch_y(self, index):
        """ Get the y position of a vertical notch

        Parameter Types:

        INDEX is an integer

        Parameter Descriptions:

        INDEX is the notch index

        """
        return self.graph_y_to_real(self.point_min + (index * (self.point_range/(NOTCHES-1))))

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
            self.canvas.create_line(
                notch_x, HORIZONTAL_BAR_Y - NOTCH_LENGTH,   # Top, X adjusted for text width
                notch_x, HORIZONTAL_BAR_Y,                  # Bottom
                fill=self.color                             # Color
            )

            # Draw Number
            self.canvas.create_text(
                notch_x,                                                    # X Position
                HORIZONTAL_TEXT_Y,                                          # Y Position
                text=self.get_number(i),   # Text
                anchor=tk.N                                                 # Cardinal Centering
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
            self.canvas.create_line(
                VERTICAL_BAR_X + FRAME_SIZE,                notch_y,    # Top, Y adjusted for text height
                VERTICAL_BAR_X + NOTCH_LENGTH + FRAME_SIZE, notch_y,    # Bottom, Y adjusted for text height
                fill=self.color                                         # Color
            )

            # region Draw Number

            # Draw the number
            self.canvas.create_text(
                VERTICAL_TEXT_X,                                            # X Position
                notch_y,                                 # Y Position
                text=self.get_number(i),   # Text
                anchor=tk.E                                                # Cardinal Centering
            )

            # endregion
