from PIL import Image
from PIL import ImageChops
from __init__ import PROJECT_PATH

if __name__ == '__main__':
    # 打开图片 1
    # 打开图片 2
    file_a = PROJECT_PATH + '/res/924935.jpg'
    imga = Image.open(file_a)
    # 打开指定的图片 2
    file_b =  PROJECT_PATH + '/res/922451.jpg'                  
    imgb = Image.open(file_b)   
    # 对两张图片进行加法运算
    ImageChops.add(imga,imgb, 1, 0).show()
    # 对两张图片进行减法运算 
    ImageChops.subtract(imga, imgb, 1, 0).show()
    # 使用变暗函数 darker()       
    ImageChops.darker(imga, imgb).show()
    # 使用变亮函数 lighter()              
    ImageChops.lighter(imga, imgb).show()
    # 将两张图片互相叠加 
    ImageChops.multiply(imga, imgb).show()
    # 实现反色后叠加
    ImageChops.screen(imga, imgb).show()
    # 使用反色函数 invert()          
    ImageChops.invert(imga).show()
    # 使用比较函数 difference()
    ImageChops.difference(imga, imga).show()        