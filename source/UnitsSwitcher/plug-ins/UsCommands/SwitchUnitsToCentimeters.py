##############################################################################
# Module:      SwitchUnitsToCentimeters
#
# Description: Defines the command "switchUnitsToCentimeters".
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

class SwitchUnitsToCentimeters(OpenMayaMPx.MPxCommand):

    def __init__(self):
        """Constructor"""
        
        OpenMayaMPx.MPxCommand.__init__(self)

        
    def doIt(self, args):
        """Command execution"""
        
        HelperFunctions.setLinearUnits(OpenMaya.MDistance.kCentimeters)