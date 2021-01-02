import numpy as np
from PIL import Image as img


def res_pic(image):
    final_list=""
    image
    #writer = open('writer_result.txt', 'w')
    try:
        image = image.convert('L')
    except:
        return "Не конвертируется"
    try:
        img_array = np.array(image)
    except:
        return "Не переводит в список"
    try:
        img_array = 256 - img_array
    except:
        return "Не инвертирует"
    try:
        ar_width, ar_height = img_array.shape
    except:
        return "Не узнаёт размер"
    try:
        img_sr = round(img_array.mean())
    except:
        return "Не округляет"
    try:
        for k in range(ar_width):
            for j in range(ar_height):
                if img_array[k, j] > round(img_sr * 1, 5):
                    final_list+=('&&')
                elif img_array[k, j] > img_sr:
                    final_list+=('||')
                elif img_array[k, j] > img_sr / 2:
                    final_list+=('__')
                else:
                    final_list+=('  ')
            final_list+=('\n')
    except:
        return "Цикл не работает"
    try:
        return final_list
    except:
        return "Не пишет"