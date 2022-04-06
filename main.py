from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys#
import random


colors = {0:"",1:"blue", 2:"green", 3:"red", 4:"brown", 5:"yellow"}
test = []
count = 0


def decision(probability):
    return random.random() < probability


def set_bombs():
    global test
    for i in range(len(test)):
        if decision(0.2) is True:
            test[i].setText("B")
            test[i].setStyleSheet("background-color: black")
            set_numbers()
        else:
            test[i].setText("")


def set_numbers():
    global test, play_width, play_height, j
    j += 1
    y = j//play_width
    x = j%play_width



def btn_hide(button):
    global count, test
    if count == 0:
        set_bombs()
        send = button.sender()
        send.hide()
        count += 1
        print("hier")
    else:
        send = button.sender()
        send.hide()
    print("pressed")


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    box_size = 30
    play_width = 16
    play_height = 30
    global colors
    for i in range(0, play_height):
        for j in range(0, play_width):
            #if i == 0:
            #    label = QLabel("")
            #else:
            #    label = QLabel(str(i))
            #num = random.choice([0,1,2,3,4,5])
            label = QLabel("")
            test.append(label)
            #label.setStyleSheet(f"background-color: lightgray; color: {colors[num]}; text-align: right")
            label.setFixedWidth(box_size)
            label.setFixedHeight(box_size)
            label.setAlignment(Qt.AlignCenter)
            grid.addWidget(label, i, j)

            button = QPushButton()
            button.setFixedWidth(box_size)
            button.setFixedHeight(box_size)
            button.clicked.connect(lambda: btn_hide(button))
            grid.addWidget(button, i, j)

    grid.setRowStretch(play_height, play_height)
    grid.setColumnStretch(play_width, play_width)
    grid.setSpacing(0)
    grid.setContentsMargins(0, 0, 0 ,0)
    win.setLayout(grid)
    win.setWindowTitle("Minesweeper")
    height = play_height*box_size
    width = play_width*box_size
    screen_height = 1080
    screen_width = 1920
    #1920 x 1080

    win.setGeometry((screen_width - width)/2, (screen_height - height)/2, width, height)
    qtrect = win.frameGeometry()
    print(qtrect)
    win.show()
    sys.exit(app.exec_())



window()
#if __name__ == '__main__':
#    window()