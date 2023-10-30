import os
import logging
from PIL import Image
from .gridmap import Gridmap

class GridmapLoader:
    
    logger = logging.getLogger('rich')
    
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
        cls.logger.info(f'Gridmap loaded: [{path}], size: {gridmap.width} x {gridmap.height} px, items: {len(gridmap.item_set)}')
        return gridmap