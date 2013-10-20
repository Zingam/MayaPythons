##############################################################################
# Module:      SwitchUnitsGUI
#
# Description: This module represents the GUI of the command "switchUnits",
#              defined in "SwitchUnits.py"
##############################################################################

# PySide imports
from PySide import QtCore
from PySide import QtGui

from shiboken import wrapInstance

# Main Maya imports
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI

# This Plug-in's imports
import HelperFunctions
reload(HelperFunctions)
import Constants
reload(Constants)


##############################################################################
# Helper functions
##############################################################################

def getMayaMainWindow():
    ptr_mainWindow = OpenMayaUI.MQtUtil.mainWindow();
    
    return wrapInstance(long(ptr_mainWindow), QtGui.QWidget)
    
    
##############################################################################
# Class Definitions
##############################################################################
    
class SwitchUnitsGUI(QtGui.QDialog):

    def __init__(self, parent=getMayaMainWindow()):
        
        super(SwitchUnitsGUI, self).__init__(parent)
        
        self.createUsDialog()
        self.setCurrentItemFromMaya()

        
    ##########################################################################
    # Class - GUI creation functions
    ##########################################################################

    def createUsDialog(self):
    
        self.setWindowTitle("Units Switcher")
        #self.setWindowFlags(QtCore.Qt.Tool)             # Use this on Mac OSX
        self.setWindowFlags(QtCore.Qt.WindowModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.createUsDialogControls()
        self.createUsDialogLayout()
        self.createSignalConnections()
    
    
    def createUsDialogControls(self):

        # Dialog label
        self.label_Dialog = QtGui.QLabel(Constants.Label_DialogText)      
        self.label_Dialog.setMargin(3)
        self.label_Dialog.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        
        # ComboBox label
        self.label_SelectUnits = QtGui.QLabel(Constants.Label_SelectUnitsText)
        
        # ComboBox
        self.comboBox_SelectUnits = QtGui.QComboBox()  
        self.comboBox_SelectUnits.addItem(Constants.ComboBoxItems['Meters'])
        self.comboBox_SelectUnits.addItem(Constants.ComboBoxItems['Centimeters'])
        self.comboBox_SelectUnits.addItem(Constants.ComboBoxItems['Millimeters'])
        
        # Push buttons
        self.pushButton_ApplyAndClose = QtGui.QPushButton(Constants.PushButton_ApplyAndCloseText)
        self.pushButton_Apply = QtGui.QPushButton(Constants.PushButton_ApplyText)
        self.pushButton_Close = QtGui.QPushButton(Constants.PushButton_CloseText)
    
    
    def createUsDialogLayout(self):
              
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setContentsMargins(5, 5, 5, 5)
        mainLayout.setSpacing(0)
        
        # BEGIN - Double dialog frame (consists of two frames - Outher0 and Outher)
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
        
        # Add the dialog label
        layout_frame_Outher.addWidget(self.label_Dialog)
        
        # BEGIN - Inner dialog frame
        self.frame_Inner = QtGui.QFrame()
        self.frame_Inner.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Sunken)
        
        layout_frame_Inner = QtGui.QGridLayout()

        # Add the combo box label
        layout_frame_Inner.addWidget(self.label_SelectUnits, 0, 0, QtCore.Qt.AlignRight)
        layout_frame_Inner.setColumnMinimumWidth(0, 100)
        
        # Add the combo box
        layout_frame_Inner.addWidget(self.comboBox_SelectUnits, 0, 1) 
        layout_frame_Inner.setColumnMinimumWidth(1, 200)
        layout_frame_Inner.setColumnStretch(1, 1)
        
        self.frame_Inner.setLayout(layout_frame_Inner)
        # END - Inner dialog frame
        
        layout_frame_Outher.addWidget(self.frame_Inner)
        layout_frame_Outher.addStretch()
        
        self.frame_Outher.setLayout(layout_frame_Outher)
        
        layout_frame_Outher0.addWidget(self.frame_Outher)
        
        self.frame_Outher0.setLayout(layout_frame_Outher0)
        # END - Double dialog frame
        
        mainLayout.addWidget(self.frame_Outher0)
        
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0, 2, 0, 2)
        self.buttonsLayout.setSpacing(2)
        
        # Add the push buttons
        self.buttonsLayout.addWidget(self.pushButton_ApplyAndClose)
        self.buttonsLayout.addWidget(self.pushButton_Apply)
        self.buttonsLayout.addWidget(self.pushButton_Close)
        
        mainLayout.addLayout(self.buttonsLayout)                
        
        self.setLayout(mainLayout)
    
    
    def createSignalConnections(self):
        
        self.pushButton_ApplyAndClose.clicked.connect(self.onClicked_pushButton_ApplyAndClose)
        self.pushButton_Apply.clicked.connect(self.onClicked_pushButton_Apply)
        self.pushButton_Close.clicked.connect(self.onClicked_pushButton_Close)
     
     
    ##########################################################################
    # Class - Slots
    ##########################################################################
    
    def onClicked_pushButton_ApplyAndClose(self):
        
        self.switchUnits()
        self.close()
        
        
    def onClicked_pushButton_Apply(self):
    
        self.switchUnits()
    
    
    def onClicked_pushButton_Close(self):
    
        self.close()


    ##########################################################################
    # Class - Helper functions
    ##########################################################################

    def switchUnits(self):
        """Switches the current units"""
        
        currentIndex = self.comboBox_SelectUnits.currentIndex()
        currentText = self.comboBox_SelectUnits.currentText()
        
        if Constants.ComboBoxItems['Meters'] == currentText:
            HelperFunctions.setLinearUnits(OpenMaya.MDistance.kMeters)
        elif Constants.ComboBoxItems['Centimeters'] == currentText:
            HelperFunctions.setLinearUnits(OpenMaya.MDistance.kCentimeters)
        elif Constants.ComboBoxItems['Millimeters'] == currentText:
            HelperFunctions.setLinearUnits(OpenMaya.MDistance.kMillimeters)
    
    
    def setCurrentItemFromMaya(self):
        """Sets the current item of the combo box to the current units)"""
        
        currentUnits = HelperFunctions.getCurrentUnits()
        index = 0
        
        if OpenMaya.MDistance.kMeters == currentUnits:
            index = self.comboBox_SelectUnits.findText(Constants.ComboBoxItems['Meters'])           
        elif OpenMaya.MDistance.kCentimeters == currentUnits:
            index = self.comboBox_SelectUnits.findText(Constants.ComboBoxItems['Centimeters'])
        elif OpenMaya.MDistance.kMillimeters == currentUnits:
            index = self.comboBox_SelectUnits.findText(Constants.ComboBoxItems['Millimeters'])
    
        self.comboBox_SelectUnits.setCurrentIndex(index)