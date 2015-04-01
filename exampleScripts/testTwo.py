
import sys

from PySide import QtGui

class Example(QtGui.QDialog):

	def __init__(self, parent=None):
		super(Example, self).__init__(parent)
		self.setGeometry(300, 300, 300, 100)
		self.setWindowTitle('Testing')

		layout = QtGui.QHBoxLayout()

		button = QtGui.QPushButton('Test Two')
		button.clicked.connect(self.test)
		layout.addWidget(button)

		self.setLayout(layout)

	def test(self):
		print 'button pressed'

def main():
	return Example()

if __name__ == '__main__':
	app = QtGui.QApplication([])
	ex = main()
	ex.show()
	sys.exit(app.exec_())
