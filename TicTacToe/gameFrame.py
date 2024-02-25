from PyQt5 import QtCore, QtGui, QtWidgets
import random
from functools import partial

class Ui_GameFrame(QtWidgets.QFrame):
    def __init__(self, platform):
        super().__init__(platform)
        self.setupUi(self)
        self.turn_num = 1
        self.mat = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        self.turnDict = {1:["O", (0, 255, 0), self.Player1_poster, self.Player1_text], -1:["X", (255, 0, 0), self.Player2_poster, self.Player2_text], 2:"DRAW"}
        self.buttonDict = {self.Grid_1:[0,0], 
                      self.Grid_2:[0,1],
                      self.Grid_3:[0,2], 
                      self.Grid_4:[1,0],
                      self.Grid_5:[1,1], 
                      self.Grid_6:[1,2], 
                      self.Grid_7:[2,0], 
                      self.Grid_8:[2,1], 
                      self.Grid_9:[2,2]}
        self.dialogues = [ "To win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.",
                          "There is a stubbornness about me that never can bear to be frightened at the will of others. My courage always rises at every attempt to intimidate me.",
                          "Mess with us and we'll do something worse than kill you. We'll kill your children.",
                          "A man who is intimate with God is not intimidated by man.",
                          "A nervous silence loosens tongues",
                          "You don't need to be so fierce and bluffing..if you already know that I can't be intimidated.",
                          "If you spend all your time thinking about how someone is going to one-up you, you can't put your best foot forward.",
                          "The ones who hate me the most are the ones who don't scare me."]
    
    def change_num(self):
        self.hide_poster_text()
        if self.turn_num == 1:
          self.turn_num = -1
          self.turnDict[self.turn_num][2].show()
          self.turnDict[self.turn_num][3].show()
          self.turnDict[self.turn_num][3].setText(random.choice(self.dialogues))
        else:
          self.turn_num = 1
          self.turnDict[self.turn_num][2].show()
          self.turnDict[self.turn_num][3].show()
          self.turnDict[self.turn_num][3].setText(random.choice(self.dialogues))

    def reset(self):
      for i in self.button_toBePressed:
          i.setEnabled(True)
          i.setText("")
      self.hide_poster_text()
      self.change_num()
      self.turn_text.setText(f"{self.turnDict[self.turn_num][0]} Turn!")
      self.mat = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
      self.restartButton.hide()
        
        
    def check_win(self, matrix):
      center = matrix[int(len(matrix)/2)][int(len(matrix)/2)]
      scoresDict = {"vert":[0 for i in range(len(matrix[0]))], "horz":[0 for i in range(len(matrix[0]))], "diag":[0, center]} # assuming all the  matrix are odd square matrix
      for row in range(len(matrix)):
        for collumn in range(len(matrix[row])):
          scoresDict["horz"][row] += matrix[row][collumn]
          scoresDict["vert"][collumn] += matrix[row][collumn]
          if row == collumn:
            scoresDict['diag'][0] += matrix[row][collumn]
          elif row  == len(matrix[row]) - collumn - 1:
            scoresDict["diag"][1] += matrix[row][collumn]
      
      for i in ['vert', 'horz', 'diag']:
          if 3 in scoresDict[i]:
             return 1
          if -3 in scoresDict[i]:
             return -1
      
      if 0 not in matrix[0] and 0 not in matrix[1] and 0 not in matrix[2]:
         return 2


    def game_start(self):
        self.show()
        self.hide_poster_text()
        self.button_toBePressed = [self.Grid_1, self.Grid_2, self.Grid_3, self.Grid_4, self.Grid_5, self.Grid_6, self.Grid_7, self.Grid_8, self.Grid_9]
        for i in self.button_toBePressed:
            i.clicked.connect(partial(self.button_push,i))
        self.turn_text.setText(f"{self.turnDict[self.turn_num][0]} Turn!")
        self.turnDict[self.turn_num][2].show()
        self.turnDict[self.turn_num][3].show()

    def hide_poster_text(self):
      poster = [self.Player1_poster, self.Player2_poster, self.Player1_text, self.Player2_text]
      for i in poster:
         i.hide()

                
    def button_push(self,button):
        button.setEnabled(False)
        x, y = self.buttonDict[button]
        self.mat[x][y] += self.turn_num
        button.setText(f"{self.turnDict[self.turn_num][0]}")
        self.change_num()
        self.turn_text.setText(f"{self.turnDict[self.turn_num][0]} Turn!")
        who_win = self.check_win(self.mat)
        if who_win is not None:
          self.hide_poster_text()
          for i in self.button_toBePressed:
            i.setEnabled(False)
          if who_win == 2:
             self.turn_text.setText(f"{self.turnDict[who_win]}!")
             self.restartButton.show()
          else:
            self.turn_text.setText(f"{self.turnDict[who_win][0]} Wins!")
            self.turnDict[who_win][2].show()
            self.turnDict[who_win][3].show()
            self.turnDict[who_win][3].setText("Nah, I'd Win!")
            self.restartButton.show()



    def setupUi(self, GameFrame):
        GameFrame.setObjectName("GameFrame")
        GameFrame.resize(340, 500)
        GameFrame.setStyleSheet("#GameFrame{\n"
                                "background-color: rgb(234, 196, 163);\n"
                                "}")
        self.Grid_1 = QtWidgets.QPushButton(GameFrame)
        self.Grid_1.setGeometry(QtCore.QRect(20, 40, 100, 100))
        self.Grid_2 = QtWidgets.QPushButton(GameFrame)
        self.Grid_2.setGeometry(QtCore.QRect(120, 40, 100, 100))
        self.Grid_3 = QtWidgets.QPushButton(GameFrame)
        self.Grid_3.setGeometry(QtCore.QRect(220, 40, 100, 100))
        self.Grid_4 = QtWidgets.QPushButton(GameFrame)
        self.Grid_4.setGeometry(QtCore.QRect(20, 140, 100, 100))
        self.Grid_5 = QtWidgets.QPushButton(GameFrame)
        self.Grid_5.setGeometry(QtCore.QRect(120, 140, 100, 100))
        self.Grid_6 = QtWidgets.QPushButton(GameFrame)
        self.Grid_6.setGeometry(QtCore.QRect(220, 140, 100, 100))
        self.Grid_7 = QtWidgets.QPushButton(GameFrame)
        self.Grid_7.setGeometry(QtCore.QRect(20, 240, 100, 100))
        self.Grid_8 = QtWidgets.QPushButton(GameFrame)
        self.Grid_8.setGeometry(QtCore.QRect(120, 240, 100, 100))
        self.Grid_9 = QtWidgets.QPushButton(GameFrame)
        self.Grid_9.setGeometry(QtCore.QRect(220, 240, 100, 100))

        self.buttons = [self.Grid_1, self.Grid_2, self.Grid_3, self.Grid_4, self.Grid_5, self.Grid_6, self.Grid_7, self.Grid_8, self.Grid_9]
        for i, buttons in enumerate(self.buttons):
        
          buttons.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
          buttons.setMouseTracking(True)
          buttons.setFocusPolicy(QtCore.Qt.StrongFocus)
          buttons.setAutoFillBackground(False)
          buttons.setStyleSheet("QPushButton{ \n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:enabled {\n"
                                  "background-color: rgb(255, 255, 255)\n"
                                  "border-radius: 0px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "background-color:  rgb(255, 255, 255);\n"
                                  "border-radius: 50px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border-radius: 50px;\n"
                                  "}\n"
                                  "QPushButton:disabled {\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 25px;\n"
                                      "font: 81 28pt Cantarell;\n"
                                      "}\n"
                                  "")
          buttons.setText("")
          buttons.setCheckable(False)
          buttons.setAutoRepeatDelay(300)
          buttons.setDefault(False)
          buttons.setObjectName(f"Grid_{i+1}")
        
        self.Player1_poster = QtWidgets.QLabel(GameFrame)
        self.Player1_poster.setGeometry(QtCore.QRect(-30, 350, 150, 160))
        self.Player1_poster.setObjectName("Player1_poster")
        self.Player2_poster = QtWidgets.QLabel(GameFrame)
        self.Player2_poster.setGeometry(QtCore.QRect(190, 350, 150, 160))
        self.Player2_poster.setObjectName("Player2_poster")

        self.p1 = QtGui.QPixmap("TicTacToe/Assets/player1.png")
        self.Player1_poster.setPixmap(self.p1.scaled(175, 175, QtCore.Qt.KeepAspectRatio))

        
        self.p2 = QtGui.QPixmap("TicTacToe/Assets/player2.png")
        self.Player2_poster.setPixmap(self.p2.scaled(175, 175, QtCore.Qt.KeepAspectRatio))



        self.turn_text = QtWidgets.QLabel(GameFrame)
        self.turn_text.setGeometry(QtCore.QRect(150, 10, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.turn_text.setFont(font)
        self.turn_text.setStyleSheet("color: rgb(0, 0, 0);")
        self.turn_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.turn_text.setText("")
        self.turn_text.setObjectName("turn_text")
        self.Player1_text = QtWidgets.QLabel(GameFrame)
        self.Player1_text.setGeometry(QtCore.QRect(120, 355, 211, 131))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Player1_text.setFont(font)
        self.Player1_text.setWordWrap(True)
        self.Player1_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Player1_text.setStyleSheet("color: rgb(0, 0, 0);")
        self.Player1_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Player1_text.setText("")
        self.Player1_text.setObjectName("Player1_text")
        self.Player2_text = QtWidgets.QLabel(GameFrame)
        self.Player2_text.setWordWrap(True)
        self.Player2_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Player2_text.setGeometry(QtCore.QRect(10, 355, 211, 131))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Player2_text.setFont(font)
        self.Player2_text.setStyleSheet("color: rgb(0, 0, 0);")
        self.Player2_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Player2_text.setText("")
        self.Player2_text.setObjectName("Player2_text")
        self.restartButton = QtWidgets.QPushButton(GameFrame)
        self.restartButton.setObjectName(u"restartButton")
        self.restartButton.setGeometry(QtCore.QRect(150, 440, 50, 50))
        self.restartButton.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"	background-color: rgb(214, 146, 111);\n"
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
        icon = QtGui.QIcon()
        icon.addFile("TicTacToe/Assets/black-panel-restart-system-icon--6.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restartButton.setIcon(icon)
        self.restartButton.hide()
        self.restartButton.clicked.connect(self.reset)

        self.retranslateUi(GameFrame)
        QtCore.QMetaObject.connectSlotsByName(GameFrame)

    def retranslateUi(self, GameFrame):
        _translate = QtCore.QCoreApplication.translate
        GameFrame.setWindowTitle(_translate("GameFrame", "GameFrame"))
