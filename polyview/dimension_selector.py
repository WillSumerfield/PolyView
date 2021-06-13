""" Dimension Selector Class for the Graph Class

Provides a GUI for selecting different available data arrays from the input data

"""

from polyview.CONSTANTS import *
import math


class DimensionSelector:

    def __init__(self, canvas, dimensions):
        """ Construct a Dimension Selector

        Parameter Types:

        CANVAS is a tkinter canvas
        DIMENSIONS is a numpy array containing tuples (label, color)

        Parameter Descriptions:

        CANVAS is the canvas to draw to
        DIMENSIONS is a list of the Dimensions people can choose to view

        """

        # region Set Parameters

        self.canvas = canvas
        self.dimensions = dimensions

        # endregion

        # region Variables

        self.current_dimension_index = 0

        # endregion

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        """ Creates a Rounded Rectangle

        Created by SneakyTurtle on StackOverFlow: https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners

        Parameter Types:

        X1, Y1, X2, Y2 are numbers
        RADIUS is a number

        Parameter Descriptions:

        X1, Y1 is the top left coordinate of the rectangle
        X2, Y2 is the bottom right coordinate of the rectangle
        radius is the radius of the rounded corners

        """

        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return self.canvas.create_polygon(points, **kwargs, smooth=True)

    def draw_horizontal(self):
        """ Draws along horizontal axis
        """

        # Draw all Dimensions
        for i in range(DIMENSIONS_SHOWN):

            # Get Dimension
            dim = self.dimensions[self.current_dimension_index + i - math.floor(DIMENSIONS_SHOWN / 2)]

            # Draw Dimension
            self.draw_dimension(
                DIMENSION_SELECTOR_SPACING + i * (DIMENSION_SIZE + DIMENSION_PADDING), 8,   # Top Left
                dim                                                                         # Dimension
            )

    def draw_vertical(self):
        pass

    def draw_dimension(self, x, y, dimension):
        """ Draws a Dimension's Clickable Box

        Parameter Types:

        X, Y are numbers
        DIMENSION is a tuple (label, color)
        OPACITY is an number such that 0 <= opacity <= 1

        Parameter Descriptions:

        X, Y are the top left coordinates for the Dimensions to be drawn at
        DIMENSION is the name and color of the Dimension
        OPACITY is the opacity of the dimensions

        """

        # Draw Rounded Rectangle
        self.round_rectangle(
            x,                  y,                      # Top Left
            x + DIMENSION_SIZE, y + DIMENSION_SIZE,     # Bottom Right
            fill=dimension[1],                         # Color
        )

        # Draw the Text in the Rounded Rectangle
        self.canvas.create_text(
            x + (DIMENSION_SIZE/2),     # Center X
            y + (DIMENSION_SIZE/2),     # Center Y
            text=dimension[0]           # Dimension Label Text
            )
