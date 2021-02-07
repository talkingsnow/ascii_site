import numpy as np
from PIL import Image as img
import os


def res_pic(image):
    final_list=""
    image = img.open(image)
    writer = open("static/writer.txt", "w")
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
        for k in range(ar_width):
            for j in range(ar_height):
                if img_array[k, j] >= 192: #round(img_sr * 1, 5):
                    final_list+=('&&')
                elif img_array[k, j] >= 128: #img_sr:
                    final_list+=('||')
                elif img_array[k, j] >= 64: #img_sr / 2:
                    final_list+=('__')
                else:
                    final_list+=('  ')
            final_list+=('\n')
    except:
        return "Цикл не работает"
    try:
        writer.write(final_list)
    except:
        return "Нет записи"