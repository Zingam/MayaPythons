from PySide import QtCore
from PySide import QtGui

from shiboken import wrapInstance

import maya.cmds as MayaCommands
import maya.OpenMayaUI as OpenMayaUI

#
# Helper functions
#

def getMayaMainWindow():
    ptr_mainWindow = OpenMayaUI.MQtUtil.mainWindow();
    
    return wrapInstance(long(ptr_mainWindow), QtGui.QWidget)
    
    
#
# Class definitions
#
    
class PluginUi(QtGui.QDialog):

    def __init__(self, parent=getMayaMainWindow()):
        
        super(PluginUi, self).__init__(parent)
        
        self.setWindowTitle("Units Switcher")
        #self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.WindowModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.createPluginUiLayout()
        
        
    def createPluginUiLayout(self):
              
        mainLayout = QtGui.QVBoxLayout()
        
        mainLayout.setContentsMargins(5, 5, 5, 5)
        mainLayout.setSpacing(0)
        
        self.frame_Outher0 = QtGui.QFrame()
        self.frame_Outher0.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Plain)
        self.frame_Outher0.setLineWidth(1)
        
        layout_frame_Outher0 = QtGui.QVBoxLayout()
        layout_frame_Outher0.setContentsMargins(1, 1, 1, 1)
        layout_frame_Outher0.setSpacing(0)
        
        self.frame_Outher = QtGui.QFrame()
        
        self.frame_Outher.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Plain)
        self.frame_Outher.setLineWidth(3)
        
        layout_frame_Outher = QtGui.QVBoxLayout()
        layout_frame_Outher.setContentsMargins(4, 4, 4, 4)
        layout_frame_Outher.setSpacing(0)
        
        self.label = QtGui.QLabel("<b>&nbsp;&nbsp;Working Units</b>")
        
        self.label.setMargin(3)
        self.label.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        
        layout_frame_Outher.addWidget(self.label)
        
        self.frame_Inner = QtGui.QFrame()
        
        self.frame_Inner.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Sunken)
        
        layout_frame_Inner = QtGui.QGridLayout()
        
        self.label_SelectUnits = QtGui.QLabel("Linear:")
        
        layout_frame_Inner.addWidget(self.label_SelectUnits, 0, 0, QtCore.Qt.AlignRight)
        layout_frame_Inner.setColumnMinimumWidth(0, 100)
        
        self.comboBox_SelectUnits = QtGui.QComboBox()
        
        self.comboBox_SelectUnits.addItem("Meters")
        self.comboBox_SelectUnits.addItem("Centimeters")
        self.comboBox_SelectUnits.addItem("Milimeters")
        
        layout_frame_Inner.addWidget(self.comboBox_SelectUnits, 0, 1) 
        layout_frame_Inner.setColumnMinimumWidth(1, 200)
        layout_frame_Inner.setColumnStretch(1, 1)
        
        self.frame_Inner.setLayout(layout_frame_Inner)
        
        layout_frame_Outher.addWidget(self.frame_Inner)

        layout_frame_Outher.addStretch()
        
        self.frame_Outher.setLayout(layout_frame_Outher)
        
        layout_frame_Outher0.addWidget(self.frame_Outher)
        
        self.frame_Outher0.setLayout(layout_frame_Outher0)
        
        mainLayout.addWidget(self.frame_Outher0)
        
        self.buttonsLayout = QtGui.QHBoxLayout()
        
        self.buttonsLayout.setContentsMargins(0, 2, 0, 2)
        self.buttonsLayout.setSpacing(2)
        
        self.pushButton_ApplyAndClose = QtGui.QPushButton("Apply and Close")
        self.pushButton_Apply = QtGui.QPushButton("Apply")
        self.pushButton_Close = QtGui.QPushButton("Close")
        
        
        self.buttonsLayout.addWidget(self.pushButton_ApplyAndClose)
        self.buttonsLayout.addWidget(self.pushButton_Apply)
        self.buttonsLayout.addWidget(self.pushButton_Close)
        
        mainLayout.addLayout(self.buttonsLayout)                
        
        self.setLayout(mainLayout)

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
