# Pyside Launch for MODO

Wraps PySide windows in a custom viewport so they can be launched within MODO.

## Installation
1. Hit Download Zip on the right
2. From MODO go to System > Open Content Folder
3. Extract the contents of the zip to the Kits folder, should be Kits/pysideLaunch

## Script Setup
- All scripts run with pyside.launch must have a main method that returns an instance of QWidget derivative
- Look at testOne.py and testTwo.py for an example setup

## Use
1. Run MODO, press the green play icon on the MODO modes toolbar, and enter the path to your script
2. You can also run ```pyside.launch {/foo/bar/someScript.py}``` from the command window
