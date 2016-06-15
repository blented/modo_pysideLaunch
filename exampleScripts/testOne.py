# launchScript "C:/dev/modo_pysideLaunch/exampleScripts/testOne.py"

import arkInit
arkInit.init()
import translators
translator = translators.getCurrent()

# import sys

from PySide import QtGui

class Example(QtGui.QWidget):

	def __init__(self, parent=None, **kwargs):
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
		confirm = QtGui.QMessageBox(self)
		confirm.setText('Awesome?')

		confirm.setInformativeText('<div style="color:red;width:50px;height:50px">Sup</div>')
		confirm.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		confirm.setDefaultButton(QtGui.QMessageBox.No)
		confirmed = confirm.exec_()

	def enterPressed(self):
		print 'text entered:', self.textEdit.text()

def main():
	return Example()

if __name__ == '__main__':
	kwargs = {}
	kwargs['options'] = {
		'title': 'Submit',
		'width': 160,
		'height': 200,
	}
	kwargs['newWindow'] = True
	translator.launch(Example, None, **kwargs)

	# app = QtGui.QApplication([])
	# ex = main()
	# ex.show()
	# sys.exit(app.exec_())
