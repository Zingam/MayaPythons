##############################################################################
# UnitsSwitcher Plug-in
#     Software:    Maya 2014
#     Version:     1.0.0.7
#     Description: Commands to quickly switch the UI units
#     Note:        Currently supports metric linear units
##############################################################################

# Python imports
import sys

sys.dont_write_bytecode = True  # Disable generating .pyc files (REMOVE!)

# Main Maya imports
import maya.OpenMayaMPx as OpenMayaMPx

# Import Plug-in's Commands
import UsCommands
reload(UsCommands)
import UsCommands.PluginShelf as PluginShelf
reload(PluginShelf)


##############################################################################
# Module definitions - constants
##############################################################################

# Global constants
cVendorName = "Roccoor Multimedia"
cPluginVersion = "1.0.0.7"

# Global variables
kPluginCommandName_switchUnits = "switchUnits"
kPluginCommandName_switchUnitsToMeters = "switchUnitsToMeters"
kPluginCommandName_switchUnitsToCentimeters = "switchUnitsToCentimeters"
kPluginCommandName_switchUnitsToMillimeters = "switchUnitsToMillimeters"
kPluginCommandName_switchUnitsHideHUD = "switchUnitsHideHUD"
kPluginCommandName_switchUnitsShowHUD = "switchUnitsShowHUD"


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


def commandCreator_switchUnitsShowHUD():
    """Create an instance of the command"""
    
    return OpenMayaMPx.asMPxPtr(UsCommands.SwitchUnitsShowHUD())

    
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
        mPlugin.registerCommand(kPluginCommandName_switchUnitsShowHUD, commandCreator_switchUnitsShowHUD)
    except:
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnits)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsToMeters)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsToCentimeters)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsToMillimeters)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsHideHUD)
        sys.stderr.write("Failed to register command: " + kPluginCommandName_switchUnitsShowHUD)
    
    # Display the HUD indication on plug-in initialization
    import maya.cmds
    maya.cmds.switchUnitsShowHUD()
    UsCommands.PluginShelf.createShelf()

    
def uninitializePlugin(mObject):
    """Uninitalizes the plugin when Maya unloads it"""
    
    # Hide the HUD indication on plug-in uninitialization
    import maya.cmds
    maya.cmds.switchUnitsHideHUD()
    UsCommands.PluginShelf.removeShelf()
    
    mPlugin = OpenMayaMPx.MFnPlugin(mObject)
    
    try:
        mPlugin.deregisterCommand(kPluginCommandName_switchUnits)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsToMeters)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsToCentimeters)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsToMillimeters)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsHideHUD)
        mPlugin.deregisterCommand(kPluginCommandName_switchUnitsShowHUD)
    except:
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnits)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsToMeters)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsToCentimeters)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsToMillimeters)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsHideHUD)
        sys.stderr.write("Failed to unregister command: " + kPluginCommandName_switchUnitsShowHUD)