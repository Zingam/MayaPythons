##############################################################################
# Module:      PluginShelf
#
# Description: Helper functions to create the plug-in shelf.
# URL:         http://forums.cgsociety.org/showthread.php?t=1091198
#              http://forums.cgsociety.org/showthread.php?t=927732
#              http://www.creativecrash.com/forums/mel/topics/delete-a-shelf-via-mel
#              http://download.autodesk.com/us/maya/2010help/API/move_tool_8py-example.html
#              http://www.creativecrash.com/forums/python/topics/plug-in-development-ui-cleanup-problem-when-maya-exits--2            
#              http://download.autodesk.com/global/docs/maya2014/en_us/PyMel/generated/functions/pymel.core.windows/pymel.core.windows.shelfButton.html#pymel.core.windows.shelfButton
##############################################################################

# Code from: http://forums.cgsociety.org/showthread.php?t=1091198

# Python imports
import maya.cmds as cmds
import maya.mel as mel

# Maya imports
import maya.cmds as cmds
import maya.mel as mel

# This Plug-in's imports
import Constants
reload(Constants)


def createShelf():
    """Create a shelf with buttons for the commands of the plug-in"""
    
    shelf = cmds.shelfLayout(Constants.ShelfName, ex=True)
    
    if shelf:
        # If the shelf already exists, clear the contents
        # and re-add thebuttons.
        newShelf = Constants.ShelfName
        buttons = cmds.shelfLayout(newShelf, query=True, childArray=True)
        if buttons:
            cmds.deleteUI(buttons, control=True)
    else:
        newShelf = mel.eval('addNewShelfTab %s' % Constants.ShelfName)
        
    cmds.setParent(newShelf)
    
    # Shelf Button - Show GUI dialog to select the UI units
    cmds.shelfButton(label=Constants.ShelfButton_GUI['label'],
                     image=Constants.ShelfButton_GUI['image'],
                     annotation=Constants.ShelfButton_GUI['annotation'],
                     command=Constants.ShelfButton_GUI['command'])
                     
    
    # Shelf Button - Show HUD indicator
    cmds.shelfButton(label=Constants.ShelfButton_ShowHUD['label'],
                     image=Constants.ShelfButton_ShowHUD['image'],
                     annotation=Constants.ShelfButton_ShowHUD['annotation'],
                     command=Constants.ShelfButton_ShowHUD['command'])
                     
    # Shelf Button - Hide HUD indicator
    cmds.shelfButton(label=Constants.ShelfButton_HideHUD['label'],
                     image=Constants.ShelfButton_HideHUD['image'],
                     annotation=Constants.ShelfButton_HideHUD['annotation'],
                     command=Constants.ShelfButton_HideHUD['command'])
                     
    # Shelf Button - Switch linear units to meters
    cmds.shelfButton(label=Constants.ShelfButton_Meters['label'],
                     image=Constants.ShelfButton_Meters['image'],
                     annotation=Constants.ShelfButton_Meters['annotation'],
                     command=Constants.ShelfButton_Meters['command'])

    # Shelf Button - Switch linear units to centimeters
    cmds.shelfButton(label=Constants.ShelfButton_Centimeters['label'],
                     image=Constants.ShelfButton_Centimeters['image'],
                     annotation=Constants.ShelfButton_Centimeters['annotation'],
                     command=Constants.ShelfButton_Centimeters['command'])

    # Shelf Button - Switch linear units to millimeters
    cmds.shelfButton(label=Constants.ShelfButton_Millimeters['label'],
                     image=Constants.ShelfButton_Millimeters['image'],
                     annotation=Constants.ShelfButton_Millimeters['annotation'],
                     command=Constants.ShelfButton_Millimeters['command'])
                     
  
def removeShelf():
    """Remove the shelf"""
    
    shelf = cmds.shelfLayout(Constants.ShelfName, ex=True)
    
    if shelf:
        mel.eval('deleteShelfTab %s' % Constants.ShelfName)
        
        # Get the main shelf from MEL's global variable: $gShelfTopLevel
        gShelfTopLevel = mel.eval('$tmpVar=$gShelfTopLevel')
        cmds.saveAllShelves(gShelfTopLevel)
    else:
        return