##############################################################################
# Module:      HelperFunctions
#
# Description: Functions that switch Maya's UI units
##############################################################################

# Python imports
import inspect

# Main Maya imports
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds

# This Plug-in's imports
import Constants
reload(Constants)


##############################################################################
# Debug Functions
##############################################################################

def printFrame(message):
    """Prints debug output."""
    pass
   
    callerframerecord = inspect.stack()[1]      # 0 represents this line
                                                # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    
    print("File:          " + info.filename)    # __FILE__     -> Test.py
    print("Function:      " + info.function)    # __FUNCTION__ -> Main
    print("Line number:   " + str(info.lineno)) # __LINE__     -> 13
   
    print("Debug message: " + message)

    
def pPP():
    """Prints the "Pew! Pew! You are dead!" message."""
    
    printFrame(Constants.PewPewDead)


##############################################################################
# Helper Functions
##############################################################################

def destroyHeadsUpDisplay():
    """Removes the HUD object of the plug-in from Maya HUD."""

    doesHUDExist = cmds.headsUpDisplay(Constants.HeadsUpDisplay['Name'], exists=True)
    
    if doesHUDExist:
        cmds.headsUpDisplay(Constants.HeadsUpDisplay['Name'], rem=True)

        
def prepareLabelText():

    return Constants.HeadsUpDisplay['linearUnits']

    
def setHeadsUpDisplay(currentUnits):
    """Displays current units on Maya HUD."""
    
    Constants.HeadsUpDisplay['linearUnits'] = currentUnits
    
    destroyHeadsUpDisplay()  # Check and destroy if a HUD object exists    
    cmds.headsUpDisplay(Constants.HeadsUpDisplay['Name'],
                        section=Constants.HeadsUpDisplay['section'],
                        block=Constants.HeadsUpDisplay['block'],
                        blockSize=Constants.HeadsUpDisplay['blockSize'],
                        label=Constants.HeadsUpDisplay['label'],
                        labelFontSize=Constants.HeadsUpDisplay['labelFontSize'],
                        command=prepareLabelText, # Every command needs
                                                  # a trigger flag (tr. flag)
                        event='SelectionChanged') # <- The (random) tr. flag
                        

##############################################################################
# Main Functions
##############################################################################

def setLinearUnits(newUnits):
    """Sets new linear units in Maya's UI."""

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
        currentUnits = Constants.ComboBoxItems['Meters']
    elif OpenMaya.MDistance.kCentimeters == newUnits:
        currentUnits = Constants.ComboBoxItems['Centimeters']
    elif OpenMaya.MDistance.kMillimeters == newUnits:
        currentUnits = Constants.ComboBoxItems['Millimeters']
        
    setHeadsUpDisplay(currentUnits)


def getCurrentUnits():
    """Retrives the current units used in Maya's UI."""
    
    return OpenMaya.MDistance.uiUnit()