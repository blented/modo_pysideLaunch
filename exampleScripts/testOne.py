
import sys

from PySide import QtGui

class Example(QtGui.QWidget):

	def __init__(self, parent=None):
		super(Example, self).__init__(parent)
		self.setGeometry(300, 300, 300, 100)
		self.setWindowTitle('Testing')

		layout = QtGui.QHBoxLayout()

		self.textEdit = QtGui.QLineEdit()
		self.textEdit.returnPressed.connect(self.enterPressed)
		layout.addWidget(self.textEdit)

		button = QtGui.QPushButton('Test One')
		button.clicked.connect(self.test)
		layout.addWidget(button)

		self.setLayout(layout)

	def test(self):
		print 'button pressed'

	def enterPressed(self):
		print 'text entered:', self.textEdit.text()

def main():
	return Example()

if __name__ == '__main__':
	app = QtGui.QApplication([])
	ex = main()
	ex.show()
	sys.exit(app.exec_())
