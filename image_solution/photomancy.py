"""[summary]
绘制随机漫步图
Returns:
    [type]: [description]
"""
from PIL import Image, ImageDraw
import random
import math
from __init__ import PROJECT_PATH


def get_random_pixel():
    # 用一个三元组的形式返回一个随机 RGB 值
    print('get_random_pixel')
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def set_to_noise(img):
    #  用随机数字替换图像的内容
    img.putdata([random.randint(0, 255) for p in range(img.width * img.height)])
    print('set_to_noise')

def get_rgb_noise(width, height):
    #  返回随机颜色像素的图像
    bands = [Image.new('L', (width, height)) for band in ('r', 'g', 'b')]
    for band in bands:
        set_to_noise(band)
    img = Image.merge('RGB', bands)
    print('get_rgb_noise')
    return img


def for_each_cell(func, img, cell_radius=1):
    # 在源图像上对像素组调用函数并返回转换后的图像
    width = img.width
    height = img.height
    img2 = Image.new(img.mode, (width, height))
    draw = ImageDraw.Draw(img2)
    for y in range(cell_radius, height-cell_radius):
        for x in range(cell_radius, width-cell_radius):
                neighbors = [img.getpixel((x_offs, y_offs)) for x_offs in range(x-cell_radius,
                    x+cell_radius+1) for y_offs in range(y-cell_radius, y+cell_radius+1)]
                func(img, draw, x, y, neighbors)
    print('for_each_cell')
    return img2


def blur(img):
    #  将每个非边界像素替换为其邻域的均值，并作为新的图像返回
    def blur_func(img, draw, x, y, neighbors):
        avg_color = get_avg_color(neighbors)
        draw.point((x, y), avg_color)
    print('blur')
    return for_each_cell(blur_func, img)


def get_avg_color(neighbors):
    # 获取平均颜色
    print('get_avg_color')
    return tuple([math.floor(sum(p[i] for p in neighbors) / len(neighbors)) for i in (0, 1, 2)])


def get_avg_value(neighbors):
    #  获取平均值
    print('get_avg_value')
    return math.floor(sum(neighbors) / len(neighbors))


def rgb_push_func(img, draw, x, y, neighbors):
    # 获取对应点的像素值
    orig_color = img.getpixel((x, y)) 
    avg_color = get_avg_color(neighbors)
    max_band_val = max(avg_color)
    pushed_color = tuple(32 if v == max_band_val else -32 for v in avg_color)
    combined_color = tuple(min(255, v[0] + v[1]) for v in zip(orig_color, pushed_color))
    # combined_color = orig_color + pushed_color
    draw.point((x, y), combined_color)


def bw_push_func(img, draw, x, y, neighbors):
    # 获取对应点的像素值 
    orig_value = img.getpixel((x, y))
    avg_value = get_avg_value(neighbors)
    # pushed_value = 32 if avg_value &gt; 127 else -32
    # combined_value = min(max（avg_value + pushed_value， 0）， 255)
    pushed_value = 255 if avg_value > 127 else 0
    draw.point((x, y), pushed_value)


def filter_color(color):
    #  颜色过滤
    if all([not(0 < v < 255) for v in color]):
        return tuple(0 if v == 255 else 255 for v in color)
    else:
        return color


if __name__ == '__main__':
    width = 800
    height = 600
    img = get_rgb_noise(width, height)
    for i in range(5):
        img = for_each_cell(rgb_push_func, img)
        img = for_each_cell(lambda img, draw, x, y, neighbors: draw.point((x, y),
            filter_color(img.getpixel((x, y)))), img, cell_radius=0)
        # img = blur（img）
    img.show()
    filename = PROJECT_PATH + '/res/mancy_output.png'
    img.save(filename)