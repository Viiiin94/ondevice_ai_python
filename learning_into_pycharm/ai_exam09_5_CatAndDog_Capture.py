import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import cv2

# python 버전이 3.10에 tensorflow==2.19.0 pyqt5==5.13.1 opencv-python==4.10.0.84 matplotlib==3.10.7 

form_window = uic.loadUiType('./cat_and_dog.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        # Exam Class는 QWidget과 form_window를 상속 받음 그래서 super()로 초기화 해줘야함
        super().__init__()
        self.path = None
        self.setupUi(self)
        self.model = load_model('./cat_and_dog_binary_classification_0.853600025177002.h5')
        # pushButton이라는 objectName을 가진 버튼 클릭 했을 때 button_slot 이벤트와 연결
        self.pushButton.clicked.connect(self.button_slot)

    def button_slot(self):
        capture = cv2.VideoCapture(0)

        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
        flag = True
        # 실제는 이미지이지만 while문을 계속 돌려서 동영상 처럼 보임
        while flag:
            ret, frame = capture.read()
            cv2.imwrite('./capture.png', frame)
            cv2.imshow('VideoFrame', frame)

            pixmap = QPixmap('.capture.png')
            self.label.setPixmap(pixmap)

            key = cv2.waitKey(33)
            if key == 27:
                flag = False

        try:
            img = Image.open('./capture.png')
            img = img.convert('RGB')
            img = img.resize((64, 64))
            data = np.asarray(img)
            data = data / 255
            data = data.reshape(1, 64, 64, 3)

            predict_value = self.model.predict(data)
            print(predict_value)
            if predict_value > 0.5:
                self.label_2.setText('개일 확률 : ' + str((predict_value[0][0] * 100).round()) + '%')
            else:
                self.label_2.setText('고양이일 확률 : ' + str((100 - predict_value[0][0] * 100).round()) + '%')

        except (IOError, OSError) as e:
            print(e)

app = QApplication(sys.argv)
mainWindow = Exam()
mainWindow.show()
sys.exit(app.exec_())



























