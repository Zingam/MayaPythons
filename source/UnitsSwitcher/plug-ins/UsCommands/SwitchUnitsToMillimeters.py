##############################################################################
# Module:      SwitchUnitsToMillimeters
#
# Description: Defines the command "switchUnitsToMillimeters".
##############################################################################

# Main Maya imports
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

# This Plug-in's imports
import HelperFunctions
reload(HelperFunctions)


##############################################################################
# Class Definitions
##############################################################################

class SwitchUnitsToMillimeters(OpenMayaMPx.MPxCommand):

    def __init__(self):
        """Constructor"""
        
        OpenMayaMPx.MPxCommand.__init__(self)

        
    def doIt(self, args):
        """Command execution"""
        
        HelperFunctions.setLinearUnits(OpenMaya.MDistance.kMillimeters)