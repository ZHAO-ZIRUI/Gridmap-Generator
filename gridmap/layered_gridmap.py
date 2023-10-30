import copy
from typing import List
import numpy as np
from .gridmap import Gridmap

class LayeredGridmap(Gridmap):
        
    def __init__(self, width: int, height: int, name='') -> None:
        self._layered_data = []
        self._overlay_mode = self.OverlayMode.KEEP_HIGH_VALUE
        self._overlay_mode_kargs = {}
        super().__init__(width, height, name)
        
    class OverlayMode:
        
        @classmethod
        def DIRECT_ADD(cls, bottom: Gridmap, top: Gridmap, kwargs):
            new = copy.deepcopy(bottom)
            new.data = bottom.data + top.data
            return new
        
        @classmethod
        def KEEP_HIGH_VALUE(cls, bottom: Gridmap, top: Gridmap, kargs):
            new = copy.deepcopy(bottom)
            new.data = np.maximum(bottom.data, top.data)
            return new
                
    @property
    def layers(self) -> List[Gridmap]:
        return self._layered_data
    
    @property
    def data(self) -> np.ndarray:
        return self.as_gridmap().data
    
    @property
    def item_set(self) -> set:
        result = set()
        for layer in self.layers:
            result.update(layer.item_set)
        return result
    
    def add_layer(self, gridmap: Gridmap):
        # check gridmap size
        if (self.width != gridmap.width) or (self.height != gridmap.height):
            self._logger.error(f'Gridmap size not match: [{self.width} x {self.height}](Origin) vs [{gridmap.width} x {gridmap.height}](New)')
            raise ValueError('Gridmap size not match')
        self._layered_data.append(gridmap)
        self._logger.info(f'Gridmap layer added: [{gridmap.name}], size {gridmap.width} x {gridmap.height} px, items: {len(gridmap.item_set)}')
        return self
    
    def add_layers(self, gridmaps: List[Gridmap]):
        for gridmap in gridmaps:
            self.add_layer(gridmap)
        self._logger.info(f'Gridmap layers added: {len(gridmaps)} layers')
        return self
        
    def set_overlay_mode(self, overlay_mode: OverlayMode, **kwargs):
        self._overlay_mode = overlay_mode
        self._overlay_mode_kargs = kwargs
        return self
    
    def replace(self, old_item: int, new_item: int):
        raise NotImplementedError('LayeredGridmap.replace() is not implemented')
    
    def as_gridmap(self) -> Gridmap:
        if len(self.layers) == 1:
            return self.layers[0].data
        layer_this = self.layers[0]
        for layer_next in self.layers[1:]:
            self._logger.debug(f'Overlaying layer: [{layer_this.name}] -> [{layer_next.name}]')
            layer_this = self._overlay_mode(layer_this, layer_next, self._overlay_mode_kargs)
        return layer_this