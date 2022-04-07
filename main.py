from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys#
import random


colors = {0:"",1:"blue", 2:"green", 3:"red", 4:"brown", 5:"yellow"}
labels_array = []
buttons_array = []
excluded = []
count = 0


def decision(probability):
    return random.random() < probability


def set_bombs(sender):
    global labels_array, buttons_array, excluded

    for i_y in range(len(labels_array)):
        for i_x in range(len(labels_array[0])):
            if buttons_array[i_y][i_x] == sender:
                set_excluded(i_y, i_x)

            if str(str(i_y) + str(i_x)) not in excluded:
                if decision(0.2) is True:
                    labels_array[i_y][i_x].setText("B")
                    labels_array[i_y][i_x].setStyleSheet("background-color: black")
                    set_numbers(i_y, i_x)
            else:
                print(f"{str(str(i_y) + str(i_x))}: \t", excluded)


def counter(y, x):
    global labels_array, colors

    label = labels_array[y][x]
    text = label.text()
    if text != "B":
        if text == "":
            text = 0
        num = int(text) + 1
        label.setText(str(num))
        label.setStyleSheet(f"color: {colors[num]}")


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


def set_excluded2(y, x):
    global labels_array, excluded

    label = labels_array[y][x]
    label.setStyleSheet("background: none")
    label.setText("")
    excluded.append(str(y) + str(x))


def set_excluded(y, x):
    set_excluded2(y + 1, x)
    set_excluded2(y, x)
    set_excluded2(y - 1, x)
    set_excluded2(y + 1, x + 1)
    set_excluded2(y, x + 1)
    set_excluded2(y - 1, x + 1)
    set_excluded2(y + 1, x - 1)
    set_excluded2(y, x - 1)
    set_excluded2(y - 1, x - 1)


def btn_hide(button):
    global count, labels_array, buttons_array
    if count == 0:
        send = button.sender()
        set_bombs(send)
        send.hide()
        count += 1
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
        labels_row = []
        buttons_row = []
        for j in range(0, play_width):
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