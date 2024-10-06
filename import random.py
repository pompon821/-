import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout, QLabel, QHBoxLayout


def randomaizer1():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(6):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()
    
def randomaizer2():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(8):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()

def randomaizer3():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(10):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()

def randomaizer4():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(12):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()

def randomaizer5():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(6):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()
    
def randomaizer6():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(8):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()

def randomaizer7():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(10):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()

def randomaizer8():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(12):
        passwords += random.choice(chars)
    winpass = QMessageBox()
    winpass.setText(passwords)
    winpass.exec_()

def h():
    randomaizer1.hide()
    randomaizer2.hide()
    randomaizer3.hide()
    randomaizer4.hide()
    randomaizer5.show()
    randomaizer6.show()
    randomaizer7.show()
    randomaizer8.show()

k=10
app = QApplication([])
win = QWidget()
win.setWindowTitle('Генератор паролей')
win.resize(300,300)
label1 = QLabel('выбери длину пароля')
button1 = QPushButton('8 символов')
button2 = QPushButton('6 символов')
button3 = QPushButton('10 символов')
button4 = QPushButton('12 символов')
button5 = QPushButton('Режим без спецсимволов')
main_lay = QVBoxLayout()
lv1 = QVBoxLayout()
lv2 = QVBoxLayout()
lv3 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

lv1.addWidget(button1)
lv1.addWidget(button2)
lv2.addWidget(button3)
lv2.addWidget(button4)
lv3.addWidget(button5)

h1.addWidget(label1)
h1.addLayout(lv3)
h2.addLayout(lv1)
h2.addLayout(lv2)
main_lay.addLayout(h1)
main_lay.addLayout(h2)

win.setLayout(main_lay)
button1.clicked.connect(randomaizer2)
button2.clicked.connect(randomaizer1)
button3.clicked.connect(randomaizer3)
button4.clicked.connect(randomaizer4)
button5.clicked.connect(h)

win.show()
app.exec_()