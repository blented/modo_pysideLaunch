
import sys
import os

import lx
import lxu
import lxifc

from PySide import QtGui

moduleName = None

class PysideWrapper(lxifc.CustomView):
	'''
	Custom viewport that imports and wraps the PySide widget
	'''

	def customview_Init(self, pane):
		'''
		Initialize the viewport, add the PySide widget.
		'''
		global moduleName
		if not (pane or moduleName):
			return False

		# Get the pane
		customPane = lx.object.CustomPane(pane)

		if not customPane.test():
			return False

		# Get the parent QWidget
		parent = customPane.GetParent()
		parentWidget = lx.getQWidget(parent)

		# Check that it suceeds
		if not parentWidget:
			return False

		# import the module we passed
		__import__(moduleName)
		# create the widget by running module.main()
		# main should return a QWidget derivative
		widget = sys.modules[moduleName].main()

		layout = QtGui.QGridLayout()
		layout.setContentsMargins(0, 0, 0, 0)

		layout.addWidget(widget)
		parentWidget.setLayout(layout)

class ShowCustomView(lxu.command.BasicCommand):
	'''
	MODO command to display the custom viewport.
	'''
	def __init__(self):
		lxu.command.BasicCommand.__init__(self)

		# define path as a require string parameter
		self.dyna_Add('Script Path', lx.symbol.sTYPE_STRING)

	def basic_Execute(self, msg, flags):
		'''
		Displays PysideWrapper in a floating palette.
		'''
		scriptPath = self.dyna_String(0)
		if not scriptPath:
			return False

		global moduleName
		# add root directory to PATH
		sys.path.insert(0, os.path.dirname(scriptPath))
		# turns /foo/bar/someScript.py into someScript
		moduleName, ext = os.path.splitext(os.path.basename(scriptPath))

		lx.eval('layout.createOrClose pysideLaunchCookie pysideLaunchLayout width:600 height:600 class:normal title:{{{0}}}'.format(moduleName))

lx.bless(PysideWrapper, 'PysideWrapper')
lx.bless(ShowCustomView, 'pyside.launch')
