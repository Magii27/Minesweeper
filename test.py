from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #setting variables
        self.colors = {0: "", 1: "blue", 2: "green", 3: "red", 4: "brown", 5: "yellow"}

        # setting title
        self.setWindowTitle("Python ")

        self.layout = QGridLayout(self)

        # setting geometry
        self.height = 500#play_height * 20
        self.width = 500 #play_width * 20
        self.screen_height = 1080
        self.screen_width = 1920
        self.setGeometry((self.screen_width - self.width)/2, (self.screen_height - self.height)/2, self.width, self.height)


        # calling method
        self.UiComponents()
        #self.setLayout(self.layout)
        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        #self.layout = QGridLayout()
        #for i_height in range(0, 16): #self.play_height):
        #    for i_width in range(0, 26): #self.play_widht):
        #        num = random.choice([0,1,2,3,4,5])
        #        label = QLabel(str(num))
        #        label.setStyleSheet(f"background-color: lightgray; color: {self.colors[num]}; text-align: right")
        #        label.setFixedWidth(20)
        #        label.setFixedHeight(20)
        #        label.setAlignment(Qt.AlignCenter)
        #        self.layout.addWidget(label, i_height, i_width)
#
        #        button = QPushButton()
        #        button.setFixedWidth(20)
        #        button.setFixedHeight(20)
        #        #self.button.clicked.connect(lambda: btn_hide(button))
        #        self.layout.addWidget(button, i_height, i_width)
#
        #        self.layout.setRowStretch(40, 40)#play_height, play_height)
        #        self.layout.setColumnStretch(40, 40)#play_width, play_width)
        #        self.layout.setSpacing(0)
        #        self.layout.setContentsMargins(0, 0, 0, 0)
        #        #win.setLayout(grid)
        #        #win.setWindowTitle("Minesweeper")
        #        #height = play_height * 20
        #        #width = play_width * 20
        #        #screen_height = 1080
        #        #screen_width = 1920
        #        # 1920 x 1080
        #        self.setLayout(self.layout)

                #win.setGeometry((screen_width - width) / 2, (screen_height - height) / 2, width, height)
                #qtrect = win.frameGeometry()

        # creating a push button
        for i_height in range(0, 16):  # self.play_height):
            for i_width in range(0, 26): #self.play_widht):
                button = QPushButton(f"{i_height}{i_width}", self)
                button.clicked.connect(lambda ch, i=i_height, clickme(i_height))
                self.layout.addWidget(button, i_height, i_width)
                #self.layout.addWidget(button, i_height, i_width)
                #button.move(i_height, i_width)
                # setting geometry of button
                #button.setGeometry(200, 150, 100, 40)
                # setting name
                #button.setAccessibleName("push button")

                # adding action to a button
                #button.clicked.connect(self.clickme)

                # accessing the name of button
                #name = button.accessibleName()
#
                ## creating a label to display a name
                #label = QLabel(self)
                #label.setText(name)
                #label.move(200, 200)

    # action method
    def clickme(self, i):
        # printing pressed
        print("pressed")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())