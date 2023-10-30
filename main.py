import cv2
from gridmap import GridmapLoader, LayeredGridmap, GridmapSaver

if __name__ == '__main__':
    
    # As default, the color of item '0' is background color (white)
    layer_1 = GridmapLoader.Load1BitBMP('./input/Layer1_Obstacle_DemoCross_1000x1000_1Bit.bmp').set_name('layer_1').replace(1, 1)
    layer_2 = GridmapLoader.Load1BitBMP('./input/Layer2_AmberLines_DemoCross_1000x1000_1Bit.bmp').set_name('layer_2').replace(1, 2)
    layer_3 = GridmapLoader.Load1BitBMP('./input/Layer3_StopLines_DemoCross_1000x1000_1Bit.bmp').set_name('layer_3').replace(1, 3)
    layer_4 = GridmapLoader.Load1BitBMP('./input/Layer4_WhiteLines_DemoCross_1000x1000_1Bit.bmp').set_name('layer_4').replace(1, 4)
    layer_5 = GridmapLoader.Load1BitBMP('./input/Layer5_CenterLines_DemoCross_1000x1000_1Bit.bmp').set_name('layer_5').replace(1, 5)
        
    lgm = LayeredGridmap(layer_1.width, layer_1.height)
    lgm.add_layers([layer_1, layer_2, layer_3, layer_4, layer_5])    
    lgm.visualizer.show_image()
    
    GridmapSaver.SaveAsNumpy(lgm, './output/layered_gridmap.npy')
    GridmapSaver.SaveAsBmp(lgm, './output/layered_gridmap.bmp')
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
