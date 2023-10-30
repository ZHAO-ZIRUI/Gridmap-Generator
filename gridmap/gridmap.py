import cv2
import numpy as np
import copy
from palttet import Palttet

class Gridmap:
    
    def __init__(self, width: int, height: int, name = '') -> None:
        self._width = width
        self._height = height
        self._name = name
        self._data = np.zeros((width, height), dtype=np.uint8)
        self._visualizer = self._GridmapVisualizer(self)
        
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def data(self) -> np.ndarray:
        return self._data
    
    @data.setter
    def data(self, new_data: np.ndarray):
        if new_data.shape != self._data.shape:
            raise ValueError(f'Gridmap size not match')
        self._data = new_data
    
    @property
    def name(self) -> str:
        if any(self._name):
            return self._name
        else:
            return f'Gridmap|{self.width} x {self.height}|{len(self.item_set)}items'
    
    @property
    def item_set(self) -> set:
        return set(self.data.flatten())
    
    def replace(self, old_item: int, new_item: int):
        self._data[self._data == old_item] = new_item
        return self
    
    def set_name(self, name: str):
        self._name = name
        return self
    
    class _GridmapVisualizer:
        
        def __init__(self, gridmap) -> None:
            self._gridmap = gridmap  # type: Gridmap
            self._item_color_map = {}
            
        @property
        def item_color_map(self) -> dict:
            result = copy.deepcopy(self._item_color_map)
            # if user defined color is empty, give the minium background color
            # WARN do not use 'result' for any() check, cause there cound have item '0' in keys
            if not any(result.values()):
                key = min(self._gridmap.item_set)
                color = Palttet.BACKGROUND_COLOR.value
                result[key] = color
            # give other items set random color
            color_iterater = Palttet.iterater()
            for item in self._gridmap.item_set:
                if item not in result:
                    result[item] = next(color_iterater).value
            return result
            
        def set_item_color(self, item: int, color):
            if not isinstance(item, int):
                raise TypeError('item must be an integer in gridmap')
            if isinstance(color, tuple):
                self._item_color_map[item] = color
            if isinstance(color, Palttet):
                self._item_color_map[item] = color.value
            return self
            
        def show_image(self):
            cv2.imshow(self._gridmap.name, self.get_visualizer_data())
            return self
        
        def get_visualizer_data(self):
            img = np.zeros((self._gridmap.height, self._gridmap.width, 3), dtype=np.uint8)
            for item, color in self.item_color_map.items():
                img[self._gridmap.data == item] = color
            return img

    @property
    def visualizer(self) -> _GridmapVisualizer:
        return self._visualizer
        