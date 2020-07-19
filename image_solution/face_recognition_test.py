"""自动识别人脸特征""" 

from PIL import Image, ImageDraw
import face_recognition
from __init__ import PROJECT_PATH
import cv2

#导入 pil 模块 

def face_recognition_test():
    # 将 jpg 文件加载到 numpy 数组中
    filename = PROJECT_PATH + '/res/willian.jpg'
    image = face_recognition.load_image_file(filename)

    # 查找图像中所有面部特征 
    face_landmarks_list = face_recognition.face_landmarks(image)

    print('I found {} face（s） in this photograph.'.format(len(face_landmarks_list)))

    for face_landmarks in face_landmarks_list:
        # 输出此图像中每个面部特征的位置 
        facial_features = [
            'chin',
            'left_eyebrow',
            'right_eyebrow',
            'nose_bridge',
            'nose_tip',
            'left_eye',
            'right_eye',
            'top_lip',
            'bottom_lip',
        ]

        for facial_feature in facial_features:
            print('The {} in this face has the following points: {}'.format(facial_feature,
                face_landmarks[facial_feature]))

        #在图像中描绘出每个人脸特征 
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)

        for facial_feature in facial_features:
            d.line(face_landmarks[facial_feature], width=5)
        pil_image.show()


def check_face_location():
    #检测人脸 
    import cv2

    #读取图片并识别人脸 
    filename = PROJECT_PATH + '/res/unknown.jpg'
    img = face_recognition.load_image_file(filename)
    face_locations = face_recognition.face_locations(img)
    print(face_locations)

    # 调用 opencv 函数显示图片 
    img = cv2.imread(filename)
    cv2.namedWindow('原图')
    cv2.imshow('原图', img)

    # 遍历每个人脸，并标注 
    faceNum = len(face_locations)
    for i in range(0, faceNum):
        top =  face_locations[i][0]
        right =  face_locations[i][1]
        bottom = face_locations[i][2]
        left = face_locations[i][3]

        start = (left, top)
        end = (right, bottom)

        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)

    #显示识别结果 
    cv2.namedWindow('识别')
    cv2.imshow('识别', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # face_recognition_test()
    check_face_location()