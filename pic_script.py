import numpy as np
from PIL import Image as img


def res_pic(image):
    try:
        writer = open('writer_result.txt', 'w')
        image = image.convert('L')

        img_array = np.array(image)
        img_array = 256 - img_array
        ar_width, ar_height = img_array.shape

        img_sr = round(img_array.mean())

        for k in range(ar_width):
            for j in range(ar_height):
                if img_array[k, j] > round(img_sr * 1, 5):
                    writer.write('&&')
                elif img_array[k, j] > img_sr:
                    writer.write('||')
                elif img_array[k, j] > img_sr / 2:
                    writer.write('__')
                else:
                    writer.write('  ')
            writer.write('\n')

    except:
        return "Изображение не получено, но не грусти, вот тебе БМП-2"

