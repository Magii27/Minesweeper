from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys#
import random


colors = {0:"",1:"blue", 2:"green", 3:"red", 4:"brown", 5:"yellow"}
labels_array = []
buttons_array = []
count = 0


def decision(probability):
    return random.random() < probability


def set_bombs():
    global labels_array
    #print(labels_array)
    for i_y in range(len(labels_array)):
        for i_x in range(len(labels_array[0])):
            if decision(0.2) is True:
                labels_array[i_y][i_x].setText("B")
                labels_array[i_y][i_x].setStyleSheet("background-color: black")
                set_numbers(i_y, i_x)


#def set_numbers():
#    global labels_array
#    #print("ich bin in set_numbers()")
#    for i_y in range(len(labels_array)):
#        for i_x in range(len(labels_array[0])):
#            #print("Text: ", labels_array[i_y][i_x].text())
#            if labels_array[i_y][i_x].text() == "B":
#                set_numbers2(i_y, i_x)


def counter(y, x):
    global labels_array
    text = labels_array[y][x].text()
    if text != "B":
        if text == "":
            text = 0
        labels_array[y][x].setText(str(int(text) + 1))
        #print(f"pos {y}/{x}: \t{str(int(text) + 1)}")


def set_numbers(y, x):
    global labels_array
    if y == 0:
        if x == 0:
            counter(y, x + 1)
            counter(y + 1, x + 1)
            counter(y + 1, x)
        elif x == len(labels_array[0]) - 1:
           counter(y, x - 1)
           counter(y + 1, x - 1)
           counter(y + 1, x)
        else:
           counter(y, x - 1)
           counter(y, x + 1)
           counter(y + 1, x - 1)
           counter(y + 1, x + 1)
           counter(y + 1, x)

    elif y == len(labels_array)-1:
        if x == 0:
            counter(y, x + 1)
            counter(y - 1, x + 1)
            counter(y - 1, x)
        elif x == len(labels_array[0]) - 1:
           counter(y, x - 1)
           counter(y - 1, x - 1)
           counter(y - 1, x)
        else:
           counter(y, x - 1)
           counter(y, x + 1)
           counter(y - 1, x - 1)
           counter(y - 1, x + 1)
           counter(y - 1, x)
    else:
        if x == 0:
            counter(y, x + 1)
            counter(y + 1, x + 1)
            counter(y - 1, x + 1)
            counter(y - 1, x)
            counter(y + 1, x)
        elif x == len(labels_array[0]) - 1:
            counter(y, x - 1)
            counter(y + 1, x - 1)
            counter(y - 1, x - 1)
            counter(y - 1, x)
            counter(y + 1, x)
        else:
           counter(y, x + 1)
           counter(y + 1, x + 1)
           counter(y - 1, x + 1)
           counter(y, x - 1)
           counter(y + 1, x - 1)
           counter(y - 1, x - 1)
           counter(y + 1, x)
           counter(y - 1, x)



def btn_hide(button):
    global count, labels_array
    if count == 0:
        set_bombs()
        send = button.sender()
        send.hide()
        count += 1
        #print("hier")
    else:
        send = button.sender()
        send.hide()
    #print("pressed")


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    box_size = 30
    play_width = 16
    play_height = 30
    global colors
    for i in range(0, play_height):
        labels_row = []
        buttons_row = []
        for j in range(0, play_width):
            #if i == 0:
            #    label = QLabel("")
            #else:
            #    label = QLabel(str(i))
            #num = random.choice([0,1,2,3,4,5])
            label = QLabel("")
            labels_row.append(label)
            #label.setStyleSheet(f"background-color: lightgray; color: {colors[num]}; text-align: right")
            label.setFixedWidth(box_size)
            label.setFixedHeight(box_size)
            label.setAlignment(Qt.AlignCenter)
            grid.addWidget(label, i, j)

            button = QPushButton()
            buttons_row.append(button)
            button.setFixedWidth(box_size)
            button.setFixedHeight(box_size)
            button.clicked.connect(lambda: btn_hide(button))
            grid.addWidget(button, i, j)

        labels_array.append(labels_row)
        buttons_array.append(buttons_row)

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

    win.setGeometry(int((screen_width - width)/2), int((screen_height - height)/2), width, height)
    qtrect = win.frameGeometry()
    print(qtrect)
    win.show()
    sys.exit(app.exec_())



window()
#if __name__ == '__main__':
#    window()