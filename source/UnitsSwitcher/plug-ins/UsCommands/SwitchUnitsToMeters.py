##############################################################################
# Module:      SwitchUnitsToMeters
#
# Description: Defines the command "switchUnitsToMeters".
##############################################################################

# Main Maya imports
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

# Import helper functions
import HelperFunctions
reload(HelperFunctions)

class SwitchUnitsToMeters(OpenMayaMPx.MPxCommand):

    def __init__(self):
        """Constructor"""
        
        OpenMayaMPx.MPxCommand.__init__(self)
        
    def doIt(self, args):
        """Command execution"""
        
        HelperFunctions.setLinearUnits(OpenMaya.MDistance.kMeters)