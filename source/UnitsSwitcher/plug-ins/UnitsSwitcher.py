##############################################################################
# UnitsSwitcher Plug-in
#     Software:    Maya 2014
#     Version:     0.0.0.5
#     Description: Commands to quickly switch the UI units
#     Note:        Currently supports metric linear units
##############################################################################

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

# Python imports
import sys

sys.dont_write_bytecode = True  # Disable generating .pyc files (REMOVE!)

# Main Maya imports
import maya.OpenMayaMPx as OpenMayaMPx

# Import Plug-in's Commands
import UsCommands
reload(UsCommands)

# Global constants
cVendorName = "Roccoor Multimedia"
cPluginVersion = "0.0.0.5"

# Global variables
kPluginCommandName_switchUnits = "switchUnits"
kPluginCommandName_switchUnitsToMeters = "switchUnitsToMeters"
kPluginCommandName_switchUnitsToCentimeters = "switchUnitsToCentimeters"
kPluginCommandName_switchUnitsToMillimeters = "switchUnitsToMillimeters"
kPluginCommandName_switchUnitsHideHUD = "switchUnitsHideHUD"

##############################################################################
# Plug-in Initialization - Helper functions
##############################################################################

def commandCreator_switchUnits():
    """Create an instance of the command"""
    
    return OpenMayaMPx.asMPxPtr(UsCommands.SwitchUnits())

    
def commandCreator_switchUnitsToMeters():
    """Create an instance of the command"""
    
    return OpenMayaMPx.asMPxPtr(UsCommands.SwitchUnitsToMeters())
    
    
def commandCreator_switchUnitsToCentimeters():
    """Create an instance of the command"""
    
    return OpenMayaMPx.asMPxPtr(UsCommands.SwitchUnitsToCentimeters())
    
    
def commandCreator_switchUnitsToMillimeters():
    """Create an instance of the command"""

    return OpenMayaMPx.asMPxPtr(UsCommands.SwitchUnitsToMillimeters())
    
    
def commandCreator_switchUnitsHideHUD():
    """Create an instance of the command"""
    
    return OpenMayaMPx.asMPxPtr(UsCommands.SwitchUnitsHideHUD())
        
##############################################################################
# Plug-in Initialization
##############################################################################

def initializePlugin(mObject):
    """Initializes the plug-in when Maya loads it"""
    
    mPlugin = OpenMayaMPx.MFnPlugin(mObject, cVendorName, cPluginVersion)
    
    try:
        mPlugin.registerCommand(kPluginCommandName_switchUnits, commandCreator_switchUnits)
        mPlugin.registerCommand(kPluginCommandName_switchUnitsToMeters, commandCreator_switchUnitsToMeters)
        mPlugin.registerCommand(kPluginCommandName_switchUnitsToCentimeters, commandCreator_switchUnitsToCentimeters)
        mPlugin.registerCommand(kPluginCommandName_switchUnitsToMillimeters, commandCreator_switchUnitsToMillimeters)
        mPlugin.registerCommand(kPluginCommandName_switchUnitsHideHUD, commandCreator_switchUnitsHideHUD)
    except:
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnits)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsToMeters)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsToCentimeters)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsToMillimeters)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsHideHUD)
        
def uninitializePlugin(mObject):
    """Uninitalizes the plugin when Maya unloads it"""
    
    mPlugin = OpenMayaMPx.MFnPlugin(mObject)
    
    try:
        mPlugin.deregisterCommand(kPluginCommandName_switchUnits)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsToMeters)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsToCentimeters)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsToMillimeters)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsHideHUD)
    except:
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnits)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsToMeters)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsToCentimeters)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsToMillimeters)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsHideHUD)