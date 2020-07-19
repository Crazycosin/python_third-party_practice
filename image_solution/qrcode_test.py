import qrcode
from PIL import Image
from __init__ import PROJECT_PATH


def store_info_test():
    data = '具体网站'
    img_file = PROJECT_PATH +  r'/res/py_qrcode.png'

    img = qrcode.make(data)
    # 图片数据保存至本地文件 
    img.save(img_file)
    # 显示二维码图片 
    img.show()


def store_info_test_1():
    img_file = PROJECT_PATH +  r'/res/dhqme_qrcode.png'
    qr = qrcode.QRCode(
     version=2,
     error_correction=qrcode.constants.ERROR_CORRECT_L,
     box_size=10,
     border=1)
    qr.add_data('具体网址')
    qr.make(fit=True)
    img = qr.make_image()
    img.save(img_file)


def store_info_test_2():
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data('具体网址')
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert('RGBA')
    bg = PROJECT_PATH + '/res/mask.jpg'
    icon = Image.open(bg)

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)
    img.show()

if __name__ == "__main__":
    # store_info_test()
    # store_info_test_1()
    store_info_test_2()