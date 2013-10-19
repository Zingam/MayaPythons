##############################################################################
# Module:      SwitchUnits
#
# Description: Defines the command "switchUnits". Has a GUI defined in the
#              module "SwitchUnitsGUI.py"
##############################################################################


# Qt - PySide imports
from shiboken import wrapInstance
from PySide import QtGui

# Main Maya imports
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

# Import custom GUI
import SwitchUnitsGUI
reload(SwitchUnitsGUI)


##############################################################################
# Class Definitions
##############################################################################

class SwitchUnits(OpenMayaMPx.MPxCommand):

    def __init__(self):
        """Constructor"""
        
        OpenMayaMPx.MPxCommand.__init__(self)
        
        
    def doIt(self, args):
        """Command execution"""
        
        try:
            ui.close()
        except:
            pass
    
        ui = SwitchUnitsGUI.SwitchUnitsGUI()
    
        ui.show()
