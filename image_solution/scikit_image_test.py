from skimage import io, data, color, img_as_float
from skimage import img_as_ubyte, data_dir
from skimage import transform
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from skimage.viewer import ImageViewer


from __init__ import PROJECT_PATH


def print_image_info_test():
    img=data.hubble_deep_field()
    print(type(img))  # 显示类型 
    print(img.shape)  # 显示尺寸 
    print(img.shape[0])  # 图片宽度 
    print(img.shape[1])  # 图片高度 
    print(img.shape[2])  # 图片通道数 
    print(img.size)   # 显示总像素数 
    print(img.max())  # 最大像素值 
    print(img.min())  # 最小像素值 
    print(img.mean()) # 平均像素值


def operate_pixel_test():
    img = data.chelsea()
    #输出图片 G 通道中第 20 行第 30 列的像素值 
    pixel = img[20, 30, 1]
    print(pixel)
    #显示猫图片红色通道的图片 
    R = img[:, :, 0]
    io.imshow(R)
    io.show()


def operate_pixel_test_1():
    img=data.chelsea()
    img_gray=color.rgb2gray(img)
    rows,cols=img_gray.shape
    for i in range(rows):
                for j in range(cols):
                    if (img_gray[i,j] <= 0.5):
                            img_gray[i,j]=0
                    else:
                            img_gray[i,j]=1
    io.imshow(img_gray)
    io.show()


def operate_pixel_test_2():
    from skimage import io, data
    img = data.chelsea()
    roi = img[150:250, 200:300, :]
    io.imshow(roi)
    io.show()


def convert_pixel_type_test():
    img = data.chelsea()
    print(img.dtype.name)

    # 进行转换
    img_grey = img_as_float(img)
    # 显示转换后的类型         
    print(img_grey.dtype.name)

    
    img = np.array([[0.2], [0.5], [0.1]], dtype=float)
    print(img.dtype.name)
    img_unit8 = img_as_ubyte(img)
    print(img_unit8.dtype.name)


def rgb2gray_test():
    image = data.chelsea()
    image_grey = color.rgb2gray(image)
    io.imshow(image_grey)
    io.show()


def hsv_test():
    image = data.chelsea()
    image_hsv = color.convert_colorspace(image, 'RGB', 'HSV')
    io.imshow(image_hsv)
    io.show()


def plot_image_test():
    #下面两行代码能保证汉字正确显示
    # 指定默认字体
    myfont = matplotlib.font_manager.FontProperties(
        fname=PROJECT_PATH + '/res/STHeitiMedium.ttc')
    # mpl.rcParams['font.sans-serif'] = ['FangSong']
    # 解决保存图像时负号显示为方块的问题
    matplotlib.rcParams['axes.unicode_minus'] = False
    filename = PROJECT_PATH + '/res/924935.jpg'
    image = io.imread(filename)
    # 创建一个名为 cat 的窗口，并设置大小
    plt.figure(num='cat', figsize=(8, 8)) 

    plt.subplot(2, 2, 1)
    plt.title(r'原始图像', fontproperties=myfont)
    plt.imshow(image)

    plt.subplot(2, 2, 2)
    plt.title(r'R 通道', fontproperties=myfont)
    plt.imshow(image[:, :, 0])

    plt.subplot(2, 2, 3)
    plt.title(r'G 通道', fontproperties=myfont)
    plt.imshow(image[:, :, 1])

    plt.subplot(2, 2, 4)
    plt.title(r'B 通道', fontproperties=myfont)
    plt.imshow(image[:, :, 2])

    plt.show()


def plot_image_test_1():
    #下面两行代码能保证汉字正确显示 
    myfont = matplotlib.font_manager.FontProperties(
        fname=PROJECT_PATH + '/res/STHeitiMedium.ttc')
    filename = PROJECT_PATH + '/res/924935.jpg'
    # 解决保存图像时负号显示为方块的问题
    matplotlib.rcParams['axes.unicode_minus'] = False 
    image = io.imread(filename)
    image_hsv = color.rgb2hsv(image)

    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    axe0, axe1, axe2, axe3 = axes.ravel()

    axe0.imshow(image)
    axe0.set_title('原始图像', fontproperties=myfont)

    axe1.imshow(image_hsv[:, :, 0])
    axe1.set_title('H 通道', fontproperties=myfont)

    axe2.imshow(image_hsv[:, :, 1])
    axe2.set_title('S 通道', fontproperties=myfont)

    axe3.imshow(image_hsv[:, :, 2])
    axe3.set_title('V 通道', fontproperties=myfont)

    for ax in axes.ravel():
        ax.axis('off')

    fig.tight_layout()

    plt.show()


def viewer_test():
    """[summary]
    at osx
    AttributeError: 'QtGui_cls' object has no attribute 'QApplication'
    """
    
    img = data.moon()
    viewer = ImageViewer(img)
    viewer.show()


def convert_collections_test():
    def convert_to_gray(f, **args):
        image = io.imread(f)
        image = color.rgb2gray(image)
        return image
    data_path = data_dir + '/*.jpg'
    collections = io.ImageCollection(data_path, load_func=convert_to_gray)
    # 显示某一张转换后的图片
    io.imshow(collections[1]) 
    io.show()


def concatenate_collections_test():
    data_path = PROJECT_PATH + '/res/92*.jpg'
    coll = io.ImageCollection(data_path)
    # 连接的图片数量
    print(len(coll))
    # 连接前的图片尺寸，所有的都一样 
    print(coll[0].shape)
    mat=io.concatenate_images(coll)
    # 连接后的数组尺寸
    print(mat.shape)


def resize_image_test():
    #下面两行代码能保证汉字正确显示
    # 解决保存图像是负号『-』显示为方块的问题
    matplotlib.rcParams['axes.unicode_minus'] = False
    myfont = matplotlib.font_manager.FontProperties(
        fname=PROJECT_PATH + '/res/STHeitiMedium.ttc')
    filename = PROJECT_PATH + '/res/924935.jpg' 
    img = io.imread(filename)
    dst=transform.resize(img, (1280, 1960))
    plt.figure('resize')
    plt.subplot(121)
    plt.title('原始图', fontproperties=myfont)
    plt.imshow(img,plt.cm.gray)
    plt.subplot(122)
    plt.title('改变后', fontproperties=myfont)
    plt.imshow(dst, plt.cm.gray)
    plt.show()


def rescale_image_test():
    filename = PROJECT_PATH + '/res/code.jpg' 
    img = data.camera()
    # 图片原始大小
    print(img.shape)
    # 缩小为原来图片的 0.1
    print(transform.rescale(img, 0.1).shape)
    # 缩小为原来图片行数的一半，列数的 1/4
    print(transform.rescale(img, [0.5, 0.25]).shape)
    # 放大为原来图片的 2 倍
    print(transform.rescale(img, 2).shape)


def rotate_image_test():
    img = data.camera()
    print(img.shape)  #图片原始大小
    img1=transform.rotate(img, 60) #旋转90度，不改变大小 
    print(img1.shape)
    img2=transform.rotate(img, 30,resize=True)  #旋转30度，同时改变大小
    print(img2.shape)   

    plt.figure('resize')

    plt.subplot(121)
    plt.title('rotate 60')
    plt.imshow(img1,plt.cm.gray)

    plt.subplot(122)
    plt.title('rotate  30')
    plt.imshow(img2,plt.cm.gray)

    plt.show()


if __name__ == "__main__":
    # print_image_info_test()
    # operate_pixel_test()
    # operate_pixel_test_1()
    # operate_pixel_test_2()
    # convert_pixel_type_test()
    # rgb2gray_test()
    # hsv_test()
    # plot_image_test()
    # plot_image_test_1()
    # viewer_test()
    # convert_collections_test()
    # concatenate_collections_test()
    # resize_image_test()
    # rescale_image_test()
    rotate_image_test()