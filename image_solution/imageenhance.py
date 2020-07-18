from PIL import (
    Image, ImageFilter,
    ImageEnhance, ImageDraw)
import os
import sys
from __init__ import PROJECT_PATH

# 素材图片的路径，能够同时处理这个目录中的所有图片 
path = PROJECT_PATH + '/res/'
dirs = os.listdir(path)


def enhancer():
    # 从文件夹中导入文件 
    for image in dirs:
        if '.jpg' not in image:
            continue
        if os.path.isfile(path+image):
            source = Image.open(path+image)
            f, e = os.path.splitext(path+image)

            # 设置两个输入图像源，分别用 DETAIL 过滤器和 FIND_EDGES 过滤器过滤图像 
            filter1 = source.filter(ImageFilter.DETAIL)
            filter2 = source.filter(ImageFilter.FIND_EDGES)

            # 一幅图像用 DETAIL 过滤器过滤，另一幅图像用 FIND_EDGES 过滤器过滤，
            # 两幅过滤后的图像混合在一起，把 alpha 设置为 0.1
            compose = Image.blend(filter1, filter2, alpha=.1)

            # 取第一个图像混合（合成）的结果并把它再次与 SMOOTH 过滤器混合，
            # 作为一个新的图像源输入，把 alpha 设置为 0.1
            filter3 = source.filter(ImageFilter.SMOOTH)
            blend = Image.blend(compose, filter3, alpha=.1)

            # 最后的混合用于移动到增强阶段。
            # 此阶段旨在增强图像的颜色 
            # IMAGE &gt; enhanced &gt; COLOR
            imageColor = ImageEnhance.Color(blend)
            renderStage1 = imageColor.enhance(1.5)

            # 此阶段旨在增强图像的对比度 
            # IMAGE（color） &gt; enhanced &gt; CONTRAST
            imageContrast = ImageEnhance.Contrast(renderStage1)
            renderStage2 = imageContrast.enhance(1.1)

            # 此阶段旨在增强图像的对比度 
            # IMAGE（contrast） &gt; enhanced &gt; BRIGHTNESS
            imageBrightness = ImageEnhance.Brightness(renderStage2)
            renderFinal = imageBrightness.enhance(1.1)

            # 最后，写入新图像文件 
            # 文件格式为 jpeg，把 quality 设置为 100
            renderFinal.save(f + '_enhanced.jpg', 'JPEG', quality=100)

if __name__ == '__main__':
    enhancer()