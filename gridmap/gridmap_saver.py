import logging
import numpy as np
from PIL import Image
from .gridmap import Gridmap

class GridmapSaver:
    
    logger = logging.getLogger('rich')
    
    @classmethod
    def SaveAsNumpy(cls, gridmap: Gridmap, filepath: str):
        if not filepath.endswith('.npy'):
            filepath += '.npy'
        np.save(filepath, gridmap.data)
        cls.logger.info(f'Gridmap saved as numpy file: [{filepath}], size: {gridmap.width} x {gridmap.height} px, items: {len(gridmap.item_set)}')
        
    @classmethod
    def SaveAsBmp(cls, gridmap: Gridmap, filepath: str):
        if not filepath.endswith('.bmp'):
            filepath += '.bmp'
        img = Image.fromarray(gridmap.visualizer.get_visualizer_data())
        img.save(filepath)
        cls.logger.info(f'Gridmap saved as bmp file: [{filepath}], size: {gridmap.width} x {gridmap.height} px, items: {len(gridmap.item_set)}')

    