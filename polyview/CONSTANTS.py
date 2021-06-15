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

# The number of notches along a dimension
NOTCHES = 10

# The length of the Notches
NOTCH_LENGTH = 2

# The size of the graph's frames
FRAME_SIZE = 2

# region Text

TEXT_HEIGHT = 16
TEXT_WIDTH = 4

TEXT_HALF_WIDTH = round(TEXT_WIDTH/2)
TEXT_HALF_HEIGHT = round(TEXT_HEIGHT/2)

# Extra space between the bar and the number text
HORIZONTAL_TEXT_PADDING = 4
VERTICAL_TEXT_PADDING = 6

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

HORIZONTAL_TEXT_STARTING_X = HORIZONTAL_BAR_X
HORIZONTAL_TEXT_Y = HORIZONTAL_BAR_Y + HORIZONTAL_TEXT_PADDING
HORIZONTAL_TEXT_NOTCH_SPACING = round(HORIZONTAL_BAR_WIDTH / NOTCHES)

# endregion

# region Vertical

VERTICAL_BAR_X = GRAPH_X - FRAME_SIZE
VERTICAL_BAR_Y = 0

VERTICAL_BAR_WIDTH = FRAME_SIZE
VERTICAL_BAR_HEIGHT = GRAPH_Y + FRAME_SIZE

VERTICAL_TEXT_X = VERTICAL_BAR_X - TEXT_WIDTH - VERTICAL_TEXT_PADDING
VERTICAL_TEXT_STARTING_Y = VERTICAL_BAR_Y + VERTICAL_BAR_HEIGHT - TEXT_HEIGHT
VERTICAL_TEXT_NOTCH_SPACING = round(VERTICAL_BAR_HEIGHT / NOTCHES)

# endregion

# endregion
