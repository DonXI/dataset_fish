from re import S
from xml.etree.ElementPath import findtext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1400, 800)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(70, 680, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setStyleSheet("#back{\n"
                                "border-radius: 10px;\n"
                                "    background-color: rgb(155, 215, 255);\n"
                                "}\n"
                                "\n"
                                "#back:hover{\n"
                                "background-color: rgb(117, 177, 255);\n"
                                "}\n"
                                "\n"
                                "#back:pressed{\n"
                                "background-color: rgb(139, 234, 255);\n"
                                "}")
        self.back.setObjectName("back")
        self.conveyor = QtWidgets.QLabel(self.centralwidget)
        self.conveyor.setGeometry(QtCore.QRect(330, 30, 51, 521))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.conveyor.setFont(font)
        self.conveyor.setStyleSheet("background-color: rgb(181, 255, 222);\n"
                                "padding:1px;")
        self.conveyor.setObjectName("conveyor")
        self.web_cam = QtWidgets.QLabel(self.centralwidget)
        self.web_cam.setGeometry(QtCore.QRect(700, 30, 671, 591))
        self.web_cam.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.web_cam.setText("")
        self.web_cam.setObjectName("web_cam")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(820, 680, 140, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(1100, 680, 140, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.select_fish_1 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_1.setGeometry(QtCore.QRect(40, 90, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_1.setFont(font)
        self.select_fish_1.setStyleSheet("#select_fish_1{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_1 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_1 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_1 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_1 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.my_data = ["เลือกชนิดปลา", "ปลาป๊อด", "ปลากุแร", "ปลาสีกุล", "ปลาทู", 
                        "ปลาข้างปาน", "ปลาหางเหลือง", "ปลาทรายแดง", "ปลาทรายดำ"]
        self.select_fish_1.setObjectName("select_fish_1")
        self.select_fish_1.addItems(self.my_data)
        self.select_fish_2 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_2.setGeometry(QtCore.QRect(40, 210, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_2.setFont(font)
        self.select_fish_2.setStyleSheet("#select_fish_2{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_2 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_2 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_2 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_2 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.select_fish_2.setObjectName("select_fish_2")
        self.select_fish_2.addItems(self.my_data)
        self.select_fish_3 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_3.setGeometry(QtCore.QRect(40, 330, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_3.setFont(font)
        self.select_fish_3.setStyleSheet("#select_fish_3{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_3 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_3 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_3 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_3 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.select_fish_3.setObjectName("select_fish_3")
        self.select_fish_3.addItems(self.my_data)
        self.select_fish_4 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_4.setGeometry(QtCore.QRect(40, 450, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_4.setFont(font)
        self.select_fish_4.setStyleSheet("#select_fish_4{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_4 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_4 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_4 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_4 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.select_fish_4.setObjectName("select_fish_4")
        self.select_fish_4.addItems(self.my_data)
        self.select_fish_8 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_8.setGeometry(QtCore.QRect(420, 450, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_8.setFont(font)
        self.select_fish_8.setStyleSheet("#select_fish_8{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_8 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_8 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_8 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_8 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.select_fish_8.setObjectName("select_fish_8")
        self.select_fish_8.addItems(self.my_data)
        self.select_fish_5 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_5.setGeometry(QtCore.QRect(420, 90, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_5.setFont(font)
        self.select_fish_5.setStyleSheet("#select_fish_5{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_5 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#select_fish_5 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#select_fish_5 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "#select_fish_5 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.select_fish_5.setObjectName("select_fish_5")
        self.select_fish_5.addItems(self.my_data)
        self.select_fish_7 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_7.setGeometry(QtCore.QRect(420, 330, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_7.setFont(font)
        self.select_fish_7.setStyleSheet("#select_fish_7{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_7 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_7 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_7 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_7 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.select_fish_7.setObjectName("select_fish_7")
        self.select_fish_7.addItems(self.my_data)
        self.select_fish_6 = QtWidgets.QComboBox(self.centralwidget)
        self.select_fish_6.setGeometry(QtCore.QRect(420, 210, 249, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_fish_6.setFont(font)
        self.select_fish_6.setStyleSheet("#select_fish_6{\n"
                                        "border-radius:5px;\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(239, 239, 239);\n"
                                        "}\n"
                                        "#select_fish_6 QListView{\n"
                                        "font-size: 12px;\n"
                                        "border: 1 px;\n"
                                        "padding:5px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_6 QListView::item{\n"
                                        "padding-left: 10 px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_6 QListView::item:hover{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#select_fish_6 QListView::item:selectrd{\n"
                                        "background-color: rgb(188, 214, 255);\n"
                                        "}")
        self.select_fish_6.setObjectName("select_fish_6")
        self.select_fish_6.addItems(self.my_data)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # 
        self.select_fish_1.currentTextChanged.connect(self.remove_data)
        self.select_fish_2.currentTextChanged.connect(self.remove_data)
        self.select_fish_3.currentTextChanged.connect(self.remove_data)
        self.select_fish_4.currentTextChanged.connect(self.remove_data)
        self.select_fish_5.currentTextChanged.connect(self.remove_data)
        self.select_fish_6.currentTextChanged.connect(self.remove_data)
        self.select_fish_7.currentTextChanged.connect(self.remove_data)
        self.select_fish_8.currentTextChanged.connect(self.remove_data)

        self.start.clicked.connect(self.select)
        self.stop.clicked.connect(self.stop_work)
        self.back.clicked.connect(exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fish sorting"))
        self.back.setText(_translate("MainWindow", "Log out"))
        self.conveyor.setText(_translate("MainWindow", "สายพาน"))
        self.stop.setText(_translate("MainWindow", "หยุดทำงาน"))
        self.start.setText(_translate("MainWindow", "เริ่มทำงาน"))
        

    # control
    def remove_data(self, text):

        if text == "เลือกชนิดปลา":
            pass
        else:
            try:
                print(text)
                self.my_data.remove(text)
                
                self.select_fish_1.clear()
                self.select_fish_2.clear()
                self.select_fish_3.clear()
                self.select_fish_4.clear()
                self.select_fish_5.clear()
                self.select_fish_6.clear()
                self.select_fish_7.clear()
                self.select_fish_8.clear()


                self.select_fish_1.addItems(self.my_data)
                self.select_fish_2.addItems(self.my_data)
                self.select_fish_3.addItems(self.my_data)
                self.select_fish_4.addItems(self.my_data)
                self.select_fish_5.addItems(self.my_data)
                self.select_fish_6.addItems(self.my_data)
                self.select_fish_7.addItems(self.my_data)
                self.select_fish_8.addItems(self.my_data)

            except:pass
            

    def select(self):
        print("start working")
        self.start.hide()
        print(self.select_fish_1.currentText())
        print(self.select_fish_2.currentText())
        print(self.select_fish_3.currentText())
        print(self.select_fish_4.currentText())
        print(self.select_fish_5.currentText())
        print(self.select_fish_6.currentText())
        print(self.select_fish_7.currentText())
        print(self.select_fish_8.currentText())
        

    def stop_work(self):
        print("stop working")
        self.start.show()

    def warning_full(self):
        msg_box_name = QMessageBox() 
        msg_box_name.setIcon(QMessageBox.Warning)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_box_name.setWindowIcon(icon)
        msg_box_name.setText("the fish is full")
        msg_box_name.setWindowTitle("Warning")
        msg_box_name.setStandardButtons(QMessageBox.Ok)
        msg_box_name.exec_()

    def error_mechanism(self):
        msg_box_name = QMessageBox() 
        msg_box_name.setIcon(QMessageBox.Warning)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
