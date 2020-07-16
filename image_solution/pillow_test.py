from PIL import Image 
from image_solution import PROJECT_PATH


def openimage_test():
    # 打开指定的图片 
    filename = PROJECT_PATH + '/res/924935.jpg'
    im = Image.open(filename)
    # 显示图片的属性信息    
    print(im.format, im.size, im.mode)
     # 显示打开的这幅图片
    im.show()


if __name__ == "__main__":
    openimage_test()