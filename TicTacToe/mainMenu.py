import sys
import webbrowser, gameFrame
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TicTacToe(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    def setupUi(self, TicTacToe):
        TicTacToe.setObjectName("TicTacToe")
        TicTacToe.setWindowModality(QtCore.Qt.WindowModal)
        TicTacToe.resize(340, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TicTacToe.sizePolicy().hasHeightForWidth())
        TicTacToe.setSizePolicy(sizePolicy)
        TicTacToe.setMinimumSize(QtCore.QSize(340, 500))
        TicTacToe.setMaximumSize(QtCore.QSize(340, 500))
        TicTacToe.setStyleSheet("background-color: rgb(234, 196, 163);")
        self.centralwidget = QtWidgets.QWidget(TicTacToe)
        self.centralwidget.setObjectName("centralwidget")
        self.created_text = QtWidgets.QLabel(self.centralwidget)
        self.created_text.setGeometry(QtCore.QRect(70, 470, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)


        self.game_frame = gameFrame.Ui_GameFrame(self)
        self.game_frame.hide()


        self.created_text.setFont(font)
        self.created_text.setStyleSheet("color: rgb(0, 0, 0);")
        self.created_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.created_text.setObjectName("created_text")
        self.p2p_button = QtWidgets.QPushButton(self.centralwidget)
        self.p2p_button.setGeometry(QtCore.QRect(70, 230, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(12)
        self.p2p_button.setFont(font)
        self.p2p_button.setStyleSheet("QPushButton{\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "border-radius: 25px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:enabled {\n"
                                      "    background-color: rgb(214, 146, 111);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:  rgb(255, 255, 255);\n"
                                      "border-radius: 25px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 25px;\n"
                                      "}"
                                      )
        self.p2p_button.setObjectName("p2p_button")
        self.p2p_button.clicked.connect(self.game_frame.game_start)
        self.p2c_button = QtWidgets.QPushButton(self.centralwidget)
        self.p2c_button.setGeometry(QtCore.QRect(70, 290, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(12)
        self.p2c_button.setFont(font)
        self.p2c_button.setStyleSheet("QPushButton{\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "border-radius: 25px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:enabled {\n"
                                      "    background-color: rgb(214, 146, 111);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:  rgb(255, 255, 255);\n"
                                      "border-radius: 25px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 25px;\n"
                                      "}")
        self.p2c_button.setObjectName("p2c_button")
        self.about_me_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_me_button.setGeometry(QtCore.QRect(70, 350, 201, 51))
        self.about_me_button.clicked.connect(lambda: webbrowser.open("https://github.com/KurtyMittens"))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(12)
        self.about_me_button.setFont(font)
        self.about_me_button.setStyleSheet("QPushButton{\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "border-radius: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:enabled {\n"
                                          "    background-color: rgb(214, 146, 111);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background-color:  rgb(255, 255, 255);\n"
                                          "border-radius: 25px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 25px;\n"
                                          "}")
        self.about_me_button.setObjectName("about_me_button")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(50, 25, 260, 200))
        self.pic = QtGui.QPixmap("TicTacToe/Assets/logo1.png")
        self.LogoLabel.setPixmap(self.pic.scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        
        self.LogoLabel.setText("")
        self.LogoLabel.setObjectName("LogoLabel")
        TicTacToe.setCentralWidget(self.centralwidget)

        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

    def retranslateUi(self, TicTacToe):
        _translate = QtCore.QCoreApplication.translate
        TicTacToe.setWindowTitle(_translate("TicTacToe", "TicTacToe"))
        self.created_text.setText(_translate("TicTacToe", "Created by KurtyMittens 2024"))
        self.p2p_button.setText(_translate("TicTacToe", "Player Vs. Player"))
        self.p2c_button.setText(_translate("TicTacToe", "UNAVAILABLE FOR NOW"))
        self.about_me_button.setText(_translate("TicTacToe", "About Me!"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    run = Ui_TicTacToe()
    sys.exit(app.exec())