""" Constants relevant to the Graph and Dimension Classes

"""

# region Window

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512

# endregion

# region Dimension Selection

DIMENSION_SIZE = 48
DIMENSION_PADDING = 8
DIMENSION_SELECTOR_SPACING = DIMENSION_SIZE + 3 * DIMENSION_PADDING
MAX_DIMENSIONS_SHOWN = 7

# endregion

# region Dimension Drawing

# region Notches

# The number of notches along a dimension
NOTCHES = 11

# The length of the Notches
NOTCH_LENGTH = 10

# endregion Notches

# The size of the graph's frames
FRAME_SIZE = 2

# region Text

TEXT_HEIGHT = 16
TEXT_WIDTH = 4

# Extra space between the bar and the number text
HORIZONTAL_TEXT_PADDING = 4
VERTICAL_TEXT_PADDING = 4

# endregion Text

# The bottom left corner of the graph
GRAPH_X = DIMENSION_SELECTOR_SPACING + FRAME_SIZE + TEXT_WIDTH + VERTICAL_TEXT_PADDING
GRAPH_Y = WINDOW_HEIGHT - DIMENSION_SELECTOR_SPACING - FRAME_SIZE - TEXT_HEIGHT - HORIZONTAL_TEXT_PADDING

# region Horizontal

# Top Left Coordinates for the Horizontal Bar
HORIZONTAL_BAR_X = GRAPH_X - FRAME_SIZE
HORIZONTAL_BAR_Y = GRAPH_Y

HORIZONTAL_BAR_WIDTH = WINDOW_WIDTH - HORIZONTAL_BAR_X
HORIZONTAL_BAR_HEIGHT = FRAME_SIZE

HORIZONTAL_NOTCH_STARTING_X = HORIZONTAL_BAR_X

HORIZONTAL_TEXT_Y = HORIZONTAL_BAR_Y + HORIZONTAL_TEXT_PADDING

# endregion

# region Vertical

VERTICAL_BAR_X = GRAPH_X - FRAME_SIZE
VERTICAL_BAR_Y = 0

VERTICAL_BAR_WIDTH = FRAME_SIZE
VERTICAL_BAR_HEIGHT = GRAPH_Y + FRAME_SIZE

VERTICAL_NOTCH_STARTING_Y = VERTICAL_BAR_Y + VERTICAL_BAR_HEIGHT - FRAME_SIZE

VERTICAL_TEXT_X = VERTICAL_BAR_X - TEXT_WIDTH - VERTICAL_TEXT_PADDING

# endregion

# endregion

# region Points

POINT_SIZE = 2
POINT_COLOR = 'black'

# endregion

# region Grid

# A proportion of the grid to add to the front and back, to make room for the points on the edges
GRID_PADDING = 0.05
GRID_COLOR = 'light gray'

# endregion