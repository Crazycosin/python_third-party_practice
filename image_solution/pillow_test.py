from PIL import Image 
from PIL import ImageFilter
from __init__ import PROJECT_PATH


def openimage_test():
    # 打开指定的图片 
    filename = PROJECT_PATH + '/res/924935.jpg'
    im = Image.open(filename)
    # 显示图片的属性信息    
    print(im.format, im.size, im.mode)
     # 显示打开的这幅图片
    im.show()


def blend_imgage_test(): 
    # 打开指定的图片 1
    file_a = PROJECT_PATH + '/res/924935.jpg'
    imga = Image.open(file_a)
    # 打开指定的图片 2
    file_b =  PROJECT_PATH + '/res/922451.jpg'
    imgb = Image.open(file_b)
    # 混合两幅图片
    Image.blend(imga, imgb, 0.3).show()


def composite_image_test():
    # 打开指定的图片 1
    file_a = PROJECT_PATH + '/res/924935.jpg'
    file_b =  PROJECT_PATH + '/res/922451.jpg'
    file_c =  PROJECT_PATH + '/res/rgba.png'
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    imga = Image.open(file_a)
    # 打开指定的图片 2
    imgb = Image.open(file_b)
    # 生成rgb文件
    # im = Image.open(file_c).convert('RGBA')
    # im.save(file_c)
    # bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    # alpha_composite = Image.alpha_composite(bg, im)
    # alpha_composite.save(file_mask, 'png', quality=80)
    # bg.paste(im, (0,0), im)
    # bg.save(file_mask)
    # 打开指定的图片 3
    mask = Image.open(file_mask)
    # 实现 3 幅图片的遮罩混合     
    Image.composite(imga, imgb, mask).show()


def eval_image_test():
    """"
    含义：使用变量function对应的函数（该函数应该有一个参数）处理变量image所代表图像中的每一个像素点。
    如果变量image所代表图像有多个通道，那变量function对应的函数作用于每一个通道。
    注意：变量function对每个像素只处理一次，所以不能使用随机组件和其他生成器。
    """
    
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    # 定义函数 div2()
    def div2(v):                         
        return v//2
    # 缩放为原来的一半
    # 打开指定的图片    
    imga = Image.open(file_mask)
    # 显示缩放后的图片      
    Image.eval(imga,div2).show()         


def thumbnail_image_test():
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    # 打开指定的图片
    imga = Image.open(file_mask)
    # 显示图像格式                
    print('图像格式:', imga.format)
    # 显示图像模式               
    print('图像模式：', imga.mode)
    # 显示图像尺寸
    print('图像尺寸：', imga.size)
    # 复制打开的图片                
    imgb = imga.copy()
    # 缩放为指定的大小                        
    imgb.thumbnail((224,168))
    # 显示缩放后的图片                      
    imgb.show()


def copy_paste_image_test():
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    imga = Image.open(file_mask)
    # 显示图像通道列表 
    print('图像通道列表：', imga.getbands())
    height = imga.height
    width = imga.width
    # 复制图片     
    imgb = imga.copy()  
    # 复制图片                        
    imgc = imga.copy()
    # 剪切指定区域的图片                   
    region = imgb.crop((width//2, height//2, width//2 + 120, height//2 + 120))
    # 粘贴的图片 
    imgc.paste(region, (0, height//2))
    # 显示粘贴后的图像
    imgc.show()


def convert_image_test():
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    # 设置要操作的指定图片 
    imga = Image.open(file_mask)
    imgb = imga.copy()
    height = imga.height
    width = imga.width
    # 创建新图像 
    img_output = Image.new('RGB', (width, height))
    img_output.paste(imgb, (0, 0))
    img_output.show()
    # 转换为 CMYK 格式的图像
    b = imgb.convert('CMYK')
    # 粘贴转换后的图像  
    img_output.paste(b, (width, 0))
    img_output.show()
    # 得到一幅左右镜像的图像 
    flip = b.transpose(Image.FLIP_LEFT_RIGHT)
    # 粘贴镜像的图像
    img_output.paste(flip, (width, 0))
    img_output.show()
    # 将图像转换为灰度图 
    b = imgb.convert('L')
    # 粘贴灰度图 
    img_output.paste(b, (width, 0))
    # 显示图片
    img_output.show()


def rotate_image_test():
    # 导入 Image 模块
    # 打开指定的图片
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    imga = Image.open(file_mask)
    height = imga.height
    width = imga.width
    # 复制打开的图片
    imgb = imga.copy()
    # 创建一个新的图像区域
    img_output = Image.new('RGB',(width//2, height//2))
    # 旋转 45°
    b = imgb.rotate(45)
    # 粘贴矩形区域                
    img_output.paste(b,(width//4, 0))
    # 输出显示图片
    img_output.show()


def merge_filter_image_test():
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    imga = Image.open(file_mask)
    height = imga.height
    width = imga.width
    chnls = imga.split() 
    # 创建一个新的图像区域
    img_output = Image.new('RGB',(width//2, height//2))
    # 分离图像通道
    # 合并 R 和 B 互换后的通道
    b = Image.merge('RGBA', chnls[::-1])
    # 粘贴合并后的图像
    img_output.paste(b, (width//4, 0))
    # 显示处理结果                   
    img_output.show()
    # 处理 R 通道中的每一个像素               
    b = imga.filter(ImageFilter.GaussianBlur)         
    img_output.paste(b, (width//4, 0))
    # 合并 R 通道中变化后的图像 
    img_output.show()


def filter_image_test():
    file_mask = PROJECT_PATH + '/res/mask.jpg'
    imgb = Image.open(file_mask)
    height = imgb.height
    width = imgb.width
    # 创建一个新的图像区域
    img_output = Image.new('RGB',(width, height))
    # 使用函数 filter()实现滤镜效果 
    b = imgb.filter(ImageFilter.GaussianBlur)
    # 粘贴指定大小的区域 
    img_output.paste(b, (0, 0))
    # 显示图片         
    img_output.show()                         


if __name__ == "__main__":
    openimage_test()
    blend_imgage_test()
    composite_image_test()
    eval_image_test()
    thumbnail_image_test()
    copy_paste_image_test()
    convert_image_test()
    rotate_image_test()
    merge_filter_image_test()
    filter_image_test()