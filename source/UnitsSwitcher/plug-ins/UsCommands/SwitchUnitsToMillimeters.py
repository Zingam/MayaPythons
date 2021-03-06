# Main Maya imports
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

# Import helper functions
import SwitchUnitsFunctions
reload(SwitchUnitsFunctions)

##############################################################################
# Class Definitions
##############################################################################

class SwitchUnitsToMillimeters(OpenMayaMPx.MPxCommand):

    def __init__(self):
        """Constructor"""
        
        OpenMayaMPx.MPxCommand.__init__(self)
        
    def doIt(self, args):
        """Command execution"""
        
        SwitchUnitsFunctions.switchUnitsToMillimeters()