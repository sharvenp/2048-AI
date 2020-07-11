
from collections import defaultdict

class Settings:

    WIDTH = 600

    BACKGROUND_COLOR = (205, 192, 180)

    # Specific colors for numbers
    # Keys are the tile exponents
    SQUARE_COLORS = {1: (238, 228, 218),
                     2: (237, 224, 200),
                     3: (242, 177, 121),
                     4: (245, 149, 99),
                     5: (246, 124, 95),
                     6: (247, 97, 72)}

    # Defualt to yellow after 64 tile
    SQUARE_COLORS = defaultdict(lambda: (228, 201, 107), SQUARE_COLORS) 

    # For light tile colors
    NUMBER_COLOR_1 = (119, 110, 101)
    # For dark tile colors
    NUMBER_COLOR_2 = (255, 255, 255)
    NUMBER_FONT = ('Hack', 40)


    LINE_COLOR = (187, 173, 160)
    LINE_WIDTH = 20


    MESSAGE_FONT = ('Hack', 40)
    MESSAGE_WIN_COLOR = (228, 211, 117)
    MESSAGE_LOSE_COLOR = (255, 120, 120)