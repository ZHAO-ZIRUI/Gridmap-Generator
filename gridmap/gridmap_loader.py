import os
from PIL import Image
from .gridmap import Gridmap

class GridmapLoader:
    
    @classmethod
    def Load1BitBMP(cls, path: str, name = '') -> Gridmap:
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        if not path.lower().endswith('.bmp'):
            raise ValueError('Only support BMP file')
        img = Image.open(path)
        gridmap = Gridmap(img.width, img.height, name)
        for y in range(img.height):
            for x in range(img.width):
                gridmap.data[x, y] = img.getpixel((x, y))
        return gridmap