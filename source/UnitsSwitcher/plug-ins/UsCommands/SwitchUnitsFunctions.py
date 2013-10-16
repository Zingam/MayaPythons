# Main Maya imports
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds


##############################################################################
# HUD object definition
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
    """Removes the HUD object of the plug-in from Maya HUD"""

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
                                                  # a trigger flag
                        event='SelectionChanged') # <- the trigger flag


##############################################################################
# Main Functions
##############################################################################

cUIUnits = "UI linear units set: "
                        
def switchUnitsToMeters():

    cUnits = "Meters"
    print(cUIUnits + cUnits)
    OpenMaya.MDistance.setUIUnit(OpenMaya.MDistance.kMeters)
    setHeadsUpDisplay("Meters")
    
    
def switchUnitsToCentimeters():

    cUnits = "Centimeters"
    print(cUIUnits + cUnits)
    OpenMaya.MDistance.setUIUnit(OpenMaya.MDistance.kCentimeters)
    setHeadsUpDisplay(cUnits)
    
    
def switchUnitsToMilimeters():

    cUnits = "Milimeters"
    print(cUIUnits + cUnits)
    #OpenMaya.MDistance.setUIUnit(OpenMaya.MDistance.kMilimeters)
    setHeadsUpDisplay(cUnits)