from PIL import (
    Image, ImageFilter,
    ImageEnhance, ImageDraw,
    ImageFont)
import os
import sys
import random
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


def filter_image_test():
    filename = PROJECT_PATH + '/res/924935.jpg'
    # 打开指定的图像
    imga = Image.open(filename) 
    # 图像的宽和高
    w, h = imga.size
    # 新建指定大小的图像
    img_output = Image.new('RGB', (2*w, h))    
    # 粘贴原始图像        
    img_output.paste(imga, (0, 0))               
    # 创建列表以存储滤镜
    fltrs = []
    # 边缘强化滤镜
    fltrs.append(ImageFilter.EDGE_ENHANCE)
    # 查找边缘滤镜 
    fltrs.append(ImageFilter.FIND_EDGES)
    # 高斯模糊滤镜
    fltrs.append(ImageFilter.GaussianBlur(4))
    # 遍历上述 3 种滤镜
    for fltr in fltrs: 
        # 使用滤镜
        r = imga.filter(fltr)
        # 粘贴使用波幅后的图像
        img_output.paste(r,(w,0))
        # 显示应用滤镜前后的图像
        img_output.show()


def draw_image_test():
    # 新建白色背景的图像
    a = Image.new('RGB', (200, 200),'white')
    # 创建绘图对象
    drw = ImageDraw.Draw(a)
    # 绘制矩形
    drw.rectangle((50, 50, 150, 150), outline='yellow')
    # 绘制文本 
    drw.text((60, 60), 'First Draw...', fill='green')
    # 显示创建二维图像
    a.show()                               


def set_image_front():
    # 设置本地字体目录
    frontfile = PROJECT_PATH + '/res/STHeitiMedium.ttc'
    ft = ImageFont.truetype(frontfile, 20)
    # 新建白色背景的图像
    a = Image.new('RGB', (200, 200),'white')
    # 创建绘图对象
    draw = ImageDraw.Draw(a)
    # 设置指定文本、字体和颜色
    draw.text((30,30), u'Python 图像处理库 PIL', font=ft, fill='red')  
    a.show()


def generate_random_alphbet():
    frontfile = PROJECT_PATH + '/res/STHeitiMedium.ttc'
    #随机字母:
    def rndChar():
        return chr(random.randint(65, 90))

    #随机颜色 1:
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    #随机颜色 2:
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    #240 * 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    #创建 Font 对象:
    font = ImageFont.truetype(frontfile, 36)
    #创建 Draw 对象:
    draw = ImageDraw.Draw(image)
    #填充每个像素:
    for x in range(width):
        for y in range(height):
                draw.point((x, y), fill=rndColor())
    #输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    #模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save(PROJECT_PATH+'/res/code.jpg', 'jpeg')


if __name__ == '__main__':
    # enhancer()
    # filter_image_test()
    # draw_image_test()
    # set_image_front()
    generate_random_alphbet()