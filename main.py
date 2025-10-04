#import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

#main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Random Word Maker')
main_window.resize(300, 200)

#create all app ojects
title_text = QLabel('Random Word Maker')
text1 = QLabel('?')
text2 = QLabel('?')
text3 = QLabel('?')

button1 = QPushButton('Click me')
button2 = QPushButton('Click me')
button3 = QPushButton('Click me')
word_list = ['A', 'B', 'C']


# All design here
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1 , alignment=Qt.AlignCenter)
row2.addWidget(text2 , alignment=Qt.AlignCenter)
row2.addWidget(text3 , alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Events here
def button1_clicked():
    word = choice(word_list)
    text1.setText(word)
def button2_clicked():
    word = choice(word_list)
    text2.setText(word)
def button3_clicked():
    word = choice(word_list)
    text3.setText(word)

button1.clicked.connect(button1_clicked)
button2.clicked.connect(button2_clicked)
button3.clicked.connect(button3_clicked)


#show/run app
main_window.show()
app.exec_()


