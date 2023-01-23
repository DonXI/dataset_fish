# show webcam(openCV) on PyQt5 : https://github.com/augmentedstartups/Face-Recogntion-PyQt/blob/master/Face_Detection_PyQt_Final/out_window.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import cv2
import torch
import torch.backends.cudnn as cudnn
from models.experimental import attempt_load
from utils.datasets import LoadStreams
from utils.general import check_img_size, non_max_suppression, scale_coords, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, TracedModel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1280, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img_fish/fish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(40, 540, 120, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit.setFont(font)
        self.exit.setStyleSheet("#exit{\n"
"border-radius: 10px;\n"
"    background-color: rgb(155, 215, 255);\n"
"}\n"
"\n"
"#exit:hover{\n"
"background-color: rgb(117, 177, 255);\n"
"}\n"
"\n"
"#exit:pressed{\n"
"background-color: rgb(139, 234, 255);\n"
"}")
        self.exit.setObjectName("exit")
        self.show_camera = QtWidgets.QLabel(self.centralwidget)
        self.show_camera.setGeometry(QtCore.QRect(610, 20, 650, 441))
        self.show_camera.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(230, 230, 230);")
        self.show_camera.setText("")
        self.show_camera.setObjectName("show_camera")
        self.img_too = QtWidgets.QLabel(self.centralwidget)
        self.img_too.setGeometry(QtCore.QRect(480, 320, 100, 40))
        self.img_too.setText("")
        self.img_too.setPixmap(QtGui.QPixmap("img_fish/too.jpg"))
        self.img_too.setScaledContents(True)
        self.img_too.setObjectName("img_too")
        self.checkBox_hang_lueang = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_hang_lueang.setGeometry(QtCore.QRect(40, 230, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_hang_lueang.setFont(font)
        self.checkBox_hang_lueang.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_hang_lueang.setObjectName("checkBox_hang_lueang")
        self.bg_fish = QtWidgets.QLabel(self.centralwidget)
        self.bg_fish.setGeometry(QtCore.QRect(20, 20, 580, 501))
        self.bg_fish.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(244, 244, 244);\n"
"")
        self.bg_fish.setText("")
        self.bg_fish.setObjectName("bg_fish")
        self.img_sai_dum = QtWidgets.QLabel(self.centralwidget)
        self.img_sai_dum.setGeometry(QtCore.QRect(480, 140, 100, 40))
        self.img_sai_dum.setText("")
        self.img_sai_dum.setPixmap(QtGui.QPixmap("img_fish/sai_dum.jpg"))
        self.img_sai_dum.setScaledContents(True)
        self.img_sai_dum.setObjectName("img_sai_dum")
        self.img_see_kun = QtWidgets.QLabel(self.centralwidget)
        self.img_see_kun.setGeometry(QtCore.QRect(190, 320, 100, 40))
        self.img_see_kun.setText("")
        self.img_see_kun.setPixmap(QtGui.QPixmap("img_fish/see_kun.jpg"))
        self.img_see_kun.setScaledContents(True)
        self.img_see_kun.setObjectName("img_see_kun")
        self.img_ku_lare = QtWidgets.QLabel(self.centralwidget)
        self.img_ku_lare.setGeometry(QtCore.QRect(480, 50, 100, 40))
        self.img_ku_lare.setText("")
        self.img_ku_lare.setPixmap(QtGui.QPixmap("img_fish/ku_lare.jpg"))
        self.img_ku_lare.setScaledContents(True)
        self.img_ku_lare.setObjectName("img_ku_lare")
        self.checkBox_pod = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pod.setGeometry(QtCore.QRect(40, 50, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_pod.setFont(font)
        self.checkBox_pod.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_pod.setObjectName("checkBox_pod")
        self.img_sai_dang = QtWidgets.QLabel(self.centralwidget)
        self.img_sai_dang.setGeometry(QtCore.QRect(190, 140, 100, 40))
        self.img_sai_dang.setText("")
        self.img_sai_dang.setPixmap(QtGui.QPixmap("img_fish/sai_dang.jpg"))
        self.img_sai_dang.setScaledContents(True)
        self.img_sai_dang.setObjectName("img_sai_dang")
        self.checkBox_sai_dang = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sai_dang.setGeometry(QtCore.QRect(40, 140, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_sai_dang.setFont(font)
        self.checkBox_sai_dang.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_sai_dang.setObjectName("checkBox_sai_dang")
        self.img_fish_all = QtWidgets.QLabel(self.centralwidget)
        self.img_fish_all.setGeometry(QtCore.QRect(300, 390, 221, 111))
        self.img_fish_all.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.img_fish_all.setStyleSheet("")
        self.img_fish_all.setText("")
        self.img_fish_all.setPixmap(QtGui.QPixmap("img_fish/mix539.jpg"))
        self.img_fish_all.setScaledContents(True)
        self.img_fish_all.setObjectName("img_fish_all")
        self.img_pod = QtWidgets.QLabel(self.centralwidget)
        self.img_pod.setGeometry(QtCore.QRect(190, 50, 100, 40))
        self.img_pod.setText("")
        self.img_pod.setPixmap(QtGui.QPixmap("img_fish/pod.jpg"))
        self.img_pod.setScaledContents(True)
        self.img_pod.setObjectName("img_pod")
        self.img_hang_lueang = QtWidgets.QLabel(self.centralwidget)
        self.img_hang_lueang.setGeometry(QtCore.QRect(190, 230, 100, 40))
        self.img_hang_lueang.setText("")
        self.img_hang_lueang.setPixmap(QtGui.QPixmap("img_fish/hang_lueang.jpg"))
        self.img_hang_lueang.setScaledContents(True)
        self.img_hang_lueang.setObjectName("img_hang_lueang")
        self.checkBox_see_kun = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_see_kun.setGeometry(QtCore.QRect(40, 320, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_see_kun.setFont(font)
        self.checkBox_see_kun.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_see_kun.setObjectName("checkBox_see_kun")
        self.checkBox_all = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_all.setGeometry(QtCore.QRect(40, 420, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_all.setFont(font)
        self.checkBox_all.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_all.setObjectName("checkBox_all")
        self.img_khang_pan = QtWidgets.QLabel(self.centralwidget)
        self.img_khang_pan.setGeometry(QtCore.QRect(480, 230, 100, 40))
        self.img_khang_pan.setText("")
        self.img_khang_pan.setPixmap(QtGui.QPixmap("img_fish/khang_pan.jpg"))
        self.img_khang_pan.setScaledContents(True)
        self.img_khang_pan.setObjectName("img_khang_pan")
        self.checkBox_ku_lare = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ku_lare.setGeometry(QtCore.QRect(330, 50, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_ku_lare.setFont(font)
        self.checkBox_ku_lare.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_ku_lare.setObjectName("checkBox_ku_lare")
        self.checkBox_sai_dum = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sai_dum.setGeometry(QtCore.QRect(330, 140, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_sai_dum.setFont(font)
        self.checkBox_sai_dum.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_sai_dum.setObjectName("checkBox_sai_dum")
        self.checkBox_khang_pan = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_khang_pan.setGeometry(QtCore.QRect(330, 230, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_khang_pan.setFont(font)
        self.checkBox_khang_pan.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_khang_pan.setObjectName("checkBox_khang_pan")
        self.checkBox_too = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_too.setGeometry(QtCore.QRect(330, 320, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_too.setFont(font)
        self.checkBox_too.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_too.setObjectName("checkBox_too")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 470, 651, 51))
        self.label.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(244, 244, 244);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(770, 540, 120, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.start.setFont(font)
        self.start.setStyleSheet("#start{\n"
"border-radius: 10px;\n"
"    background-color: rgb(169, 255, 175);\n"
"}\n"
"\n"
"#start:hover{\n"
"background-color: rgb(117, 255, 149);\n"
"}\n"
"\n"
"#start:pressed{\n"
"background-color: rgb(186, 255, 160);\n"
"}")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(1070, 540, 120, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stop.setFont(font)
        self.stop.setStyleSheet("#stop{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 206, 206);\n"
"}\n"
"\n"
"#stop:hover{\n"
"background-color: rgb(255, 156, 156);\n"
"}\n"
"\n"
"#stop:pressed{\n"
"background-color: rgb(255, 197, 221);\n"
"}")
        self.stop.setObjectName("stop")
        self.bg_fish.raise_()
        self.exit.raise_()
        self.show_camera.raise_()
        self.img_too.raise_()
        self.img_sai_dum.raise_()
        self.img_see_kun.raise_()
        self.img_ku_lare.raise_()
        self.checkBox_pod.raise_()
        self.img_sai_dang.raise_()
        self.checkBox_sai_dang.raise_()
        self.img_fish_all.raise_()
        self.img_pod.raise_()
        self.img_hang_lueang.raise_()
        self.checkBox_see_kun.raise_()
        self.checkBox_all.raise_()
        self.img_khang_pan.raise_()
        self.checkBox_ku_lare.raise_()
        self.checkBox_sai_dum.raise_()
        self.checkBox_khang_pan.raise_()
        self.checkBox_too.raise_()
        self.checkBox_hang_lueang.raise_()
        self.label.raise_()
        self.start.raise_()
        self.stop.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.checkBox_all.stateChanged.connect(self.select_all)
        self.start.clicked.connect(self.start_work)
        self.stop.clicked.connect(self.stop_work)
        self.exit.clicked.connect(self.stop_exit)

        self.retranslateUi(MainWindow)
        self.start.pressed.connect(self.show_camera.clear)
        self.stop.pressed.connect(self.show_camera.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fish sorting"))
        self.exit.setText(_translate("MainWindow", "exit"))
        self.checkBox_hang_lueang.setText(_translate("MainWindow", "ปลาหางเหลือง"))
        self.checkBox_pod.setText(_translate("MainWindow", "ปลาป๊อด"))
        self.checkBox_sai_dang.setText(_translate("MainWindow", "ปลาทรายแดง"))
        self.checkBox_see_kun.setText(_translate("MainWindow", "ปลาสีกุล"))
        self.checkBox_all.setText(_translate("MainWindow", "ปลา 8 สายพันธุ์"))
        self.checkBox_ku_lare.setText(_translate("MainWindow", "ปลากุแร"))
        self.checkBox_sai_dum.setText(_translate("MainWindow", "ปลาทรายดำ"))
        self.checkBox_khang_pan.setText(_translate("MainWindow", "ปลาข้างปาน"))
        self.checkBox_too.setText(_translate("MainWindow", "ปลาทู"))
        self.start.setText(_translate("MainWindow", "start"))
        self.stop.setText(_translate("MainWindow", "stop"))

    # checkbox select all 
    def select_all(self, state):
        checkboxs = [self.checkBox_hang_lueang, self.checkBox_khang_pan, self.checkBox_pod, self.checkBox_ku_lare,
                        self.checkBox_see_kun, self.checkBox_too, self.checkBox_sai_dang, self.checkBox_sai_dum]
        for checkbox in checkboxs:
            checkbox.setCheckState(state)

    # type fish checked 
    def check(self):
        if self.checkBox_hang_lueang.isChecked():
            print("hang_lueang")
        if self.checkBox_khang_pan.isChecked():
            print("khang_pan")
        if self.checkBox_pod.isChecked():
            print("pod")
        if self.checkBox_ku_lare.isChecked():
            print("ku_lare")
        if self.checkBox_see_kun.isChecked():
            print("see_kun")
        if self.checkBox_too.isChecked():
            print("too")
        if self.checkBox_sai_dang.isChecked():
            print("sai_dang")
        if self.checkBox_sai_dum.isChecked():
            print("sai_dum")
        else:
            self.show_label("please select")
            self.start.show()

    # start work after selected checkbox
    def start_work(self):
        self.check()
        self.start.hide()
        weights=['yolov7_3200.pt'] 
        source='0' 
        img_size=640
        conf_thres=0.25
        iou_thres=0.45
        device='cpu'
        classes=None
        agnostic_nms=False
        augment=False
        trace=True
        imgsz=img_size

        webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))

        # Initialize
        set_logging()
        device = select_device(device)
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(weights, map_location=device)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        imgsz = check_img_size(imgsz, s=stride)  # check img_size

        if trace:
            model = TracedModel(model, device, img_size)

        if half:
            model.half()  # to FP16

        # Set Dataloader
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)

        # Get names and colors
        names = model.module.names if hasattr(model, 'module') else model.names

        # Run inference
        if device.type != 'cpu':
            model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
        old_img_w = old_img_h = imgsz
        old_img_b = 1

        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Warmup
            if device.type != 'cpu' and (old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
                old_img_b = img.shape[0]
                old_img_h = img.shape[2]
                old_img_w = img.shape[3]
                for i in range(3):
                    model(img, augment=augment)[0]

            # Inference
            pred = model(img, augment=augment)[0]

            # Apply NMS
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes=classes, agnostic=agnostic_nms)

            # Process detections
            for i, det in enumerate(pred):  # detections per image
                result = ''
                if webcam:  # batch_size >= 1
                    s, im0 = '%g: ' % i, im0s[i].copy()
                else:
                    s, im0 = '', im0s
                
                #print('len(det) :', len(det))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
                        result = names[int(c)]
                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        label = f'{names[int(cls)]} {conf:.2f}'
                        #result = label
                        plot_one_box(xyxy, im0, label=label, color=names[int(cls)], line_thickness=2, name = str(names[int(cls)]))

                # Stream results
                self.display_image(im0)
                print(result)

        
    def display_image(self, frame):
        frame = cv2.resize(frame, (1920, 1080))
        qformat = QImage.Format_Indexed8
        if len(frame.shape) == 3:
            if frame.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(frame, frame.shape[1], frame.shape[0], qformat)
        outImage = outImage.rgbSwapped()
        # show frame video on gui
        self.show_camera.setPixmap(QPixmap.fromImage(outImage))
        self.show_camera.setScaledContents(True)

    def show_label(self, name):
        self.label.setText(name)

    def stop_work(self):
        self.start.show()

    def stop_exit(self):
        #self.show_label("press again to exit !!!")
        self.stop_work()
        self.exit.clicked.connect(exit)

    def warning_full(self):
        msg_box_name = QMessageBox() 
        msg_box_name.setIcon(QMessageBox.Warning)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img_fish/fish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_box_name.setWindowIcon(icon)
        msg_box_name.setText("the fish is full")
        msg_box_name.setWindowTitle("Warning")
        msg_box_name.setStandardButtons(QMessageBox.Ok)
        msg_box_name.exec_()

    def error_mechanism(self):
        msg_box_name = QMessageBox() 
        msg_box_name.setIcon(QMessageBox.Warning)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img_fish/fish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_box_name.setWindowIcon(icon)
        msg_box_name.setText("Error mechanism")
        msg_box_name.setWindowTitle("Warning")
        msg_box_name.setStandardButtons(QMessageBox.Ok)
        self.stop_work()
        msg_box_name.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
