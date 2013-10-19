##############################################################################
# Module:      SwitchUnitsShowHUD
#
# Description: Defines the command "switchUnitsShowHUD".
##############################################################################

# Main Maya imports
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

# Import helper functions
import HelperFunctions
reload(HelperFunctions)

##############################################################################
# Class Definitions
##############################################################################

class SwitchUnitsShowHUD(OpenMayaMPx.MPxCommand):

    def __init__(self):
        """Constructor"""
        
        OpenMayaMPx.MPxCommand.__init__(self)
        
    def doIt(self, args):
        """Command execution"""
        
        currentUnits = OpenMaya.MDistance.uiUnit()
    
        if OpenMaya.MDistance.kMeters == currentUnits:
            currentUnits = "Meters"
        elif OpenMaya.MDistance.kCentimeters == currentUnits:
            currentUnits = "Centimeters"
        elif OpenMaya.MDistance.kMillimeters == currentUnits:
            currentUnits = "Millimeters"
        
        HelperFunctions.setHeadsUpDisplay(currentUnits)