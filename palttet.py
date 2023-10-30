from enum import Enum

class Palttet(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    CYAN = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    ORANGE = (0, 165, 255)
    PURPLE = (128, 0, 128)
    PINK = (203, 192, 255)
    LIME = (0, 255, 0)
    TEAL = (128, 128, 0)
    BROWN = (42, 42, 165)
    GREY = (128, 128, 128)
    SILVER = (192, 192, 192)
    GOLD = (0, 215, 255)
    VIOLET = (211, 0, 148)
    INDIGO = (130, 0, 75)
    MAROON = (0, 69, 139)
    # define special color
    BACKGROUND_COLOR = WHITE
    ACCENT_COLOR = MAGENTA
                
    @classmethod
    def iterater(cls):
        while True:
            for color in cls:
                if color is None:
                    continue
                if color is cls.BACKGROUND_COLOR:
                    continue
                if color is cls.ACCENT_COLOR:
                    continue
                yield color
