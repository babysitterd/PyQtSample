import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Square:
	def __init__(self, width, height):
		self.width = width
		self.height = height

SCREEN_SIZE = Square(3840, 2160)
WINDOW_SIZE = Square(1024, 768)
CHARACTER_WINDOW_SIZE = Square(500, 500)

def center_window_coords(screen, window):
	return int((screen.width - window.width) / 2), \
	       int((screen.height - window.height) / 2) 

class CharacterWindow(QWidget):
	def __init__(self, character, parent = None):
		super(CharacterWindow, self).__init__(parent)
		self.setWindowTitle(character)
		# show character image
		vbox = QVBoxLayout()
		labelImage = QLabel(self)
		pixmap = QPixmap(f"./{character}.jpg")
		labelImage.setPixmap(pixmap)
		vbox.addWidget(labelImage)
		self.setLayout(vbox)

class MainWindow(QWidget):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		characters = ['RUY', 'CHUN-LI', 'NASH']
		BUTTON_HEIGHT = 32
		x = 10
		for character in characters:
			character_button = QPushButton(character, self)
			character_button.move(15, x)
			x = x + BUTTON_HEIGHT
			character_button.clicked.connect(self.openCharacterWindow)

	def openCharacterWindow(self):
		character = self.sender().text()
		self.sub = CharacterWindow(character)
		x, y = center_window_coords(SCREEN_SIZE, CHARACTER_WINDOW_SIZE)
		self.sub.setGeometry(x, y, CHARACTER_WINDOW_SIZE.width, CHARACTER_WINDOW_SIZE.height)
		self.sub.show()

def run():
	application = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.setWindowTitle('Street Fighter V Frame Data')

	x, y = center_window_coords(SCREEN_SIZE, WINDOW_SIZE)
	main_window.setGeometry(x, y, WINDOW_SIZE.width, WINDOW_SIZE.height)	
	main_window.show()

	application.exec_()

run()