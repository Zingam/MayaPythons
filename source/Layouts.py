#
# main - Program entry point
#        
        
if __name__ == "__main__":
    
    # Work around PySide bug when opening too many windows
    try:
        ui.close()
    except:
        pass
    
    ui = PluginUi()
    
    ui.show()
    
'''
    
'''    
# System
# System
import sys
import os
 
# GUI Modules
from PySide import QtCore, QtGui
import maya.OpenMayaUI as apiUI
 
# Allows converting pointers to Python objects
from shiboken import wrapInstance
 
def maya_main_window():
    main_win_ptr = apiUI.MQtUtil.mainWindow()
    return wrapInstance(long(main_win_ptr), QtGui.QWidget)
 
# Create out Dialog class, inheriting from QDialog
class Dialog(QtGui.QDialog):
 
    # Call the maya_main_window command to parent it
    def __init__(self, parent = maya_main_window()):
 
        super(Dialog, self).__init__(parent)
 
        # Create a list of rows and buttons
        self.rows = ["Row1", "Row2", "Row3"]
        self.buttons = ["Button1", "Button2", "Button3"]
 
        # And now set up the UI
        self.setup_ui()
 
    def setup_ui(self):
 
        self.main_layout = QtGui.QVBoxLayout()
 
        # Create a series of rows, and in each row, put our buttons
        for row in self.rows:
 
            self.row_Hbox = QtGui.QGroupBox()
            self.layout = QtGui.QGridLayout()
 
            for button in self.buttons:
 
                # Label the button with it's list name
                self.push_button = QtGui.QPushButton(button, self)
 
                # Give each button a unique object name
                self.b_name = row + "_" + button
                self.push_button.setObjectName(self.b_name)
 
                # Add a QLine Edit to each particular button
                self.q_line_name = self.b_name + "_TextEdit"
                self.my_line_edit = QtGui.QLineEdit()
                self.my_line_edit.setText("Hi! I'm " + self.q_line_name)
                 
                # Also give it a unique name
                self.my_line_edit.setObjectName(self.q_line_name)
 
                # Offset each button in the layout by it's index number
                self.layout.addWidget(self.push_button, 0, self.buttons.index(button))
 
                # Offset each QLine Edit in the layout to be underneath each button
                self.layout.addWidget(self.my_line_edit, 1, self.buttons.index(button))                
 
                # Connect the button to an event
                self.push_button.clicked.connect(self.on_button_event)
 
            # Add the buttons to our layout
            self.row_Hbox.setLayout(self.layout)
            self.main_layout.addWidget(self.row_Hbox)
 
        # Set the layout and title
        self.setLayout(self.main_layout)
        self.setWindowTitle("Example Window")
 
    def on_button_event(self):
 
        sender = self.sender()
        print sender.objectName() + ' was pressed'
 
        # Get the text from the text line edit linked with the button
        self.line_edit_name = sender.objectName() + "_TextEdit"
        self.line_edit = self.findChild(QtGui.QLineEdit, self.line_edit_name)
        print self.line_edit
        print self.line_edit.text()
 
# Call our dialog   
dialog = Dialog()
dialog.show()
