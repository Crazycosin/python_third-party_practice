'''
@Descripttion: 
@version: 
@Author: crazycosin
@Date: 2020-07-18 20:50:29
@LastEditors: crazycosin
@LastEditTime: 2020-07-20 21:56:19
'''
from PIL import Image, ImageDraw
import photomancy
import random
from __init__ import PROJECT_PATH


if __name__ == "__main__":
    width, height = (800, 600)
    img = Image.new('L', (width, height))
    photomancy.set_to_noise(img)
    for i in range(5):
        img = photomancy.for_each_cell(photomancy.bw_push_func, img, cell_radius=3)
        img.show()
    filename = PROJECT_PATH + '/res/caves_output.png'
    img.save(filename)