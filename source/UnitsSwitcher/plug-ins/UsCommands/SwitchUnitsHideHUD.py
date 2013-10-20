##############################################################################
# Module:      SwitchUnitsHideHUD
#
# Description: Defines the command "switchUnitsHideHUD".
##############################################################################

# Main Maya imports
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

# This Plug-in's imports
import HelperFunctions
reload(HelperFunctions)


##############################################################################
# Class Definitions
##############################################################################

class SwitchUnitsHideHUD(OpenMayaMPx.MPxCommand):

    def __init__(self):
        """Constructor"""
        
        OpenMayaMPx.MPxCommand.__init__(self)
        
        
    def doIt(self, args):
        """Command execution"""
        
        HelperFunctions.destroyHeadsUpDisplay()