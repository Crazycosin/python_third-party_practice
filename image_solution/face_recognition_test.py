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


def face_recognition_test_1():
    # 识别图片中的所有人脸并显示出来 
    # filename : shibie02.py
    # 导入 pil 模块 
    # 导入 face_recogntion 模块，可用命令安装 pip install face_recognition

    # 将 jpg 文件加载到 numpy 数组中
    filename = PROJECT_PATH + '/res/unknown.jpg'
    image = face_recognition.load_image_file(filename)

    # 使用默认的 HOG 模型查找图像中所有人脸 
    # 这个方法已经相当准确了，但还是不如 CNN 模型那么准确，因为没有使用 GPU 加速 
    # 另见 find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    # 使用 CNN 模型 
    # face_locations = face_recognition.face_locations（image， number_of_times_to_upsample=0，
        # model=「cnn」）

    # 显示从图片中找到了多少张人脸 
    print('I found {} face（s）in this photograph.'.format(len(face_locations)))

    # 循环找到的所有人脸 
    for face_location in face_locations:
          # 显示每张脸的位置信息 
        top, right, bottom, left = face_location
        print('Top: {}, Left: {}, Bottom: {}, Right: {}'.format(top, left, bottom, right))
        # 指定人脸的位置信息，然后显示人脸图片 
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()


def face_recognition_test_2():
    # 识别图片中的人脸 
    wi_filename = PROJECT_PATH + '/res/willian.jpg'
    ma_filename = PROJECT_PATH + '/res/maria.jpg'
    unknown_filename = PROJECT_PATH + '/res/unknown.jpg'
    jobs_image = face_recognition.load_image_file(wi_filename)
    obama_image = face_recognition.load_image_file(ma_filename)
    unknown_image = face_recognition.load_image_file(unknown_filename)

    laoguan_encoding = face_recognition.face_encodings(jobs_image)[0]
    maomao_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([laoguan_encoding, maomao_encoding], unknown_encoding)
    labels = ['willian', 'maria']

    print('结果:' + str(results))

    for i in range(0, len(results)):
        if results[i] == True:
                print('这个人是:' + labels[i])


def face_recognition_test_3():
    # 笔记本电脑的摄像头是 0，外接摄像头是 1
    video_capture = cv2.VideoCapture(0)
    wi_filename = PROJECT_PATH + '/res/willian.jpg'
    ma_filename = PROJECT_PATH + '/res/maria.jpg'
    obama_img = face_recognition.load_image_file(wi_filename)
    obama_face_encoding = face_recognition.face_encodings(obama_img)[0]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        if process_this_frame:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                    match = face_recognition.compare_faces([obama_face_encoding], face_encoding)
                    if match[0]:
                        name = 'willian'
                    else:
                        name = 'unknown'
                    face_names.append(name)
        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),  2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # face_recognition_test()
    # check_face_location()
    # face_recognition_test_1()
    # face_recognition_test_2()
    face_recognition_test_3()