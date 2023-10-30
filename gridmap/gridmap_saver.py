import numpy as np
from PIL import Image
from .gridmap import Gridmap

class GridmapSaver:
    
    @classmethod
    def SaveAsNumpy(cls, gridmap: Gridmap, filepath: str):
        if not filepath.endswith('.npy'):
            filepath += '.npy'
        np.save(filepath, gridmap.data)
        
    @classmethod
    def SaveAsBmp(cls, gridmap: Gridmap, filepath: str):
        if not filepath.endswith('.bmp'):
            filepath += '.bmp'
        img = Image.fromarray(gridmap.visualizer.get_visualizer_data())
        img.save(filepath)
        
    