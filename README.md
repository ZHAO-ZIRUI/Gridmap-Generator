# GridMap-Generator

The most easy way to generate or composite gridmap from 1-bit BMP format in the manner specified by you and provide visualization during the process.

![](/docs/banner.jpg)

### Requirements

- Python: 3.8 +

### Using Steps

1. Install python requirements

    ```
    pip install -f requirements.txt
    ```

2. Edit 1-bit bmp formatted gridmap via Photoshop

    > Black area represents `1` and white area represents `0` 

3. Modify `main.py` file to fit your requirements

    a. Load 1-bit bmp formatted gridmap

        ```
        layer_n = GridmapLoader.Load1BitBMP('<file_path_to_1bit_bmp_file>', '<alias_name>')
        ``` 

    b. Replace `1` to your defined data and add them to layers

        ```
        layers.append(layer_n.replace(1, <user_defined_data_int>))
        ```

    c. Edit output file

        ```
        GridmapSaver.SaveAsNumpy(lgm, '<out_put_file_name>')
        ```

### About

This project is designed for autonomous driving development. If you have any questions, you can submit an issue or communicate via email.