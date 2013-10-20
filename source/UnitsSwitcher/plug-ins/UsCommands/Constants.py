##############################################################################
# Module:      Constants
#
# Description: Defines all global constants in one place.
##############################################################################

##############################################################################
# HUD indicator constants
##############################################################################

HeadsUpDisplay = {
    'Name'          : "HUDCurrentUnits",
    'section'       : 2,
    'block'         : 0,
    'blockSize'     : "medium",
    'label'         : "Linear units:",
    'labelFontSize' : "small",
    'linearUnits'   : ""
}


##############################################################################
# Dialog
##############################################################################

# ComboBox constants
ComboBoxItems = {
    'Meters'     : "Meters",
    'Centimeters': "Centimeters",
    'Millimeters': "Millimeters"
}

# Labels
Label_DialogText      = "<b>&nbsp;&nbsp;Working Units</b>"
Label_SelectUnitsText = "Linear"

# Buttons
PushButton_ApplyAndCloseText = "Apply and Close"
PushButton_ApplyText         = "Apply"
PushButton_CloseText         = "Close"


##############################################################################
# Shelf
##############################################################################
ShelfName = "UnitsSwitcher"

ShelfButton_GUI = {
    'label'     : "GUI",
    'image'     : "button_GUI.png",
    'annotation': "UnitsSwitcher: Open dialog",
    'style'     : "iconOnly",
    'command'   : "maya.cmds.switchUnits()"
}

ShelfButton_ShowHUD = {
    'label'     : "ShowHUD",
    'image'     : "button_showHUD.png",
    'annotation': "UnitsSwitcher: Show HUD indicator",
    'style'     : "iconOnly",
    'command'   : "maya.cmds.switchUnitsShowHUD()"
}

ShelfButton_HideHUD = {
    'label'     : "HideHUD",
    'image'     : "button_hideHUD.png",
    'annotation': "UnitsSwitcher: Hide HUD indicator",
    'style'     : "iconOnly",
    'command'   : "maya.cmds.switchUnitsHideHUD()"
}

ShelfButton_Meters = {
    'label'     : "Meters",
    'image'     : "button_meters.png",
    'annotation': "UnitsSwitcher: Switch linear units to meters",
    'style'     : "iconOnly",
    'command'   : "maya.cmds.switchUnitsToMeters()"
}

ShelfButton_Centimeters = {
    'label'     : "Centimeters",
    'image'     : "button_centimeters.png",
    'annotation': "UnitsSwitcher: Switch linear units to centimeters",
    'style'     : "iconOnly",
    'command'   : "maya.cmds.switchUnitsToCentimeters()"
}

ShelfButton_Millimeters = {
    'label'     : "Millimeters",
    'image'     : "button_millimeters.png",
    'annotation': "UnitsSwitcher: Switch linear units to millimeters",
    'style'     : "iconOnly",
    'command'   : "maya.cmds.switchUnitsToMillimeters()"
}


##############################################################################
# Debug strings
##############################################################################

PewPewDead = "Pew! Pew! You are dead!"


##################################################################################################
# Maximum Line Length
# PEP 8 -- Style Guide for Python Code
# http://www.python.org/dev/peps/pep-0008/#maximum-line-length
##################################################################################################
# 99 characters per line #########################################################################
#########################################################################################
# 90 characters per line ################################################################
##############################################################################
# 79 characters per line - Python Library ####################################
#######################################################################
# 72 characters per line - docstrings/comments ########################
##################################################################################################