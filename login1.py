from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main1 import Ui_MainWindow

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(550, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Login.setFont(font)
        Login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Login.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius:5px;")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(190, 460, 141, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_login.sizePolicy().hasHeightForWidth())
        self.button_login.setSizePolicy(sizePolicy)
        self.button_login.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_login.setFont(font)
        self.button_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_login.setMouseTracking(False)
        self.button_login.setAcceptDrops(False)
        self.button_login.setStyleSheet("#button_login{\n"
"    border-radius: 20px;\n"
"    background-color: rgb(255, 230, 255);\n"
"}\n"
"#button_login:hover{\n"
"background-color: rgb(255, 170, 255);\n"
"}\n"
"#button_login:pressed{\n"
"background-color: rgb(211, 230, 255);\n"
"}")
        self.button_login.setObjectName("button_login")
        self.enter_username = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_username.setGeometry(QtCore.QRect(120, 300, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_username.sizePolicy().hasHeightForWidth())
        self.enter_username.setSizePolicy(sizePolicy)
        self.enter_username.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.enter_username.setFont(font)
        self.enter_username.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.enter_username.setStyleSheet("border-radius:5px;\n"
"padding-left:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.enter_username.setObjectName("enter_username")
        self.enter_password = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_password.setGeometry(QtCore.QRect(120, 370, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_password.sizePolicy().hasHeightForWidth())
        self.enter_password.setSizePolicy(sizePolicy)
        self.enter_password.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.enter_password.setFont(font)
        self.enter_password.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.enter_password.setStyleSheet("border-radius:5px;\n"
"padding-left:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.enter_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter_password.setObjectName("enter_password")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(190, 90, 161, 141))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("fish.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)
        self.button_login.clicked.connect(self.show_login)
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.button_login.setText(_translate("Login", "Log in"))
        self.enter_username.setPlaceholderText(_translate("Login", "Username"))
        self.enter_password.setPlaceholderText(_translate("Login", "Password"))
    
    def show_login(self):
        print("button_login")
        self.login_send(self.enter_username.text(), self.enter_password.text())
        
    def login_send(self, user, password):
        self.data_login = {"test": "test1", "admin": "admin1"}
        if user in self.data_login.keys() and password == self.data_login[user]:
            print("show second window")
            self.main = QtWidgets.QMainWindow()
            self.ui_main = Ui_MainWindow()
            self.ui_main.setupUi(self.main)
            Login.hide()
            self.main.show()
            
        else:
            print("Invalid username or password")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
