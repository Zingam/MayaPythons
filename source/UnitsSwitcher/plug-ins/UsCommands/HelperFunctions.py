# Main Maya imports
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds

import Constants

##############################################################################
# Module definitions - constants
##############################################################################

headsUpDisplay = {
    'Name'          : "HUDCurrentUnits",
    'section'       : 2,
    'block'         : 0,
    'blockSize'     : "medium",
    'label'         : "Linear units:",
    'labelFontSize' : "small",
    'linearUnits'   : ""
}


##############################################################################
# Helper Functions
##############################################################################

def destroyHeadsUpDisplay():
    """Removes the HUD object of the plug-in from Maya HUD."""

    doesHUDExist = cmds.headsUpDisplay(headsUpDisplay['Name'], exists=True)
    
    if doesHUDExist:
        cmds.headsUpDisplay(headsUpDisplay['Name'], rem=True)

        
def prepareLabelText():

    return headsUpDisplay['linearUnits']

    
def setHeadsUpDisplay(currentUnits):
    """Displays current units on Maya HUD."""

    headsUpDisplay['linearUnits'] = currentUnits
    
    destroyHeadsUpDisplay()  # Check and destroy if a HUD object exists    
    cmds.headsUpDisplay(headsUpDisplay['Name'],
                        section=headsUpDisplay['section'],
                        block=headsUpDisplay['block'],
                        blockSize=headsUpDisplay['blockSize'],
                        label=headsUpDisplay['label'],
                        labelFontSize=headsUpDisplay['labelFontSize'],
                        command=prepareLabelText, # Every command needs
                                                  # a trigger flag (tr. flag)
                        event='SelectionChanged') # <- The (random) tr. flag


##############################################################################
# Main Functions
##############################################################################

def setLinearUnits(newUnits):
    """Sets new linear units in Maya's UI..."""
    pass

    # Save the current grid
    currentGridSpacing = cmds.grid(query=True, spacing=True)
    currentGridSize = cmds.grid(query=True, size=True)
  
    # Set the new units used in the UI
    OpenMaya.MDistance.setUIUnit(newUnits)
    
    # Restore the grid
    cmds.grid(spacing=currentGridSpacing, size=currentGridSize)
    
    # Prepare the HUD indication
    currentUnits = "Unknown"
    
    # CAUTION: Re-using argument "newUnits"
    newUnits = OpenMaya.MDistance.uiUnit()
    
    if OpenMaya.MDistance.kMeters == newUnits:
        currentUnits = "Meters"
    elif OpenMaya.MDistance.kCentimeters == newUnits:
        currentUnits = "Centimeters"
    elif OpenMaya.MDistance.kMillimeters == newUnits:
        currentUnits = "Millimeters"
        
    setHeadsUpDisplay(currentUnits)


def getCurrentUnits():
    """Retrives the current units used in Maya's UI"""
    
    return OpenMaya.MDistance.uiUnit()