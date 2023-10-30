import cv2
import logging
from gridmap import GridmapLoader, LayeredGridmap, GridmapSaver
from rich.logging import RichHandler

logging.basicConfig(level=logging.DEBUG, format="%(message)s", datefmt="[%X]", handlers=[RichHandler(highlighter=None)])

if __name__ == '__main__':
    logger = logging.getLogger("rich")
    logger.info("Program start!")
    
    # load gridmaps
    logger.info('Loading 1-bit BMP file as Gridmap')
    layer_1 = GridmapLoader.Load1BitBMP('./input/Layer1_Obstacle_DemoCross_1000x1000_1Bit.bmp', 'Layer 1 Obstacle')
    layer_2 = GridmapLoader.Load1BitBMP('./input/Layer2_AmberLines_DemoCross_1000x1000_1Bit.bmp', 'Layer 2 AmberLines')
    layer_3 = GridmapLoader.Load1BitBMP('./input/Layer3_StopLines_DemoCross_1000x1000_1Bit.bmp', 'Layer 3 StopLines')
    layer_4 = GridmapLoader.Load1BitBMP('./input/Layer4_WhiteLines_DemoCross_1000x1000_1Bit.bmp', 'Layer 4 WhiteLines')
    layer_5 = GridmapLoader.Load1BitBMP('./input/Layer5_CenterLines_DemoCross_1000x1000_1Bit.bmp', 'Layer 5 CenterLines')
    
    # reformate gridmap and save to list
    layers = []
    layers.append(layer_1.replace(1, 1))
    layers.append(layer_2.replace(1, 2))
    layers.append(layer_3.replace(1, 3))
    layers.append(layer_4.replace(1, 4))
    layers.append(layer_5.replace(1, 5))
    
    # generate layered gridmap
    logger.info('Creating LayeredGridmap and apply overlay mode')
    lgm = LayeredGridmap(layer_1.width, layer_1.height)
    lgm.add_layers(layers)
    
    # show images
    logger.info(f'Show layers and overlayed images')
    for layer in layers:
        layer.visualizer.show_image()
    lgm.visualizer.show_image()
    logger.warning(f'Please press any key or close all windows to continue ...')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    logger.info('Saving LayeredGridmap as numpy and bmp file')
    GridmapSaver.SaveAsNumpy(lgm, './output/layered_gridmap.npy')
    GridmapSaver.SaveAsBmp(lgm, './output/layered_gridmap.bmp')
    
    logger.info('Program end!')
