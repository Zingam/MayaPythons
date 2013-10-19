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
def createMyShelf():
	shelfName = 'My_Shelf'
	test = cmds.shelfLayout(shelfName, ex=True)
	if test:
		# If the shelf already exists, clear the contents and re-add the buttons.
		newShelf = shelfName
		buttons = cmds.shelfLayout(newShelf, query=True, childArray=True)
		cmds.deleteUI(buttons, control=True)	   
	else:
		newShelf = mel.eval('addNewShelfTab %s' % shelfName)	   
	cmds.setParent(newShelf)
	# add buttons here
    
    
def removeShelf():
	shelfName = 'My_Shelf'
	test = cmds.shelfLayout(shelfName, ex=True)
	if test:
		mel.eval('deleteShelfTab %s' % shelfName)
		gShelfTopLevel = mel.eval('$tmpVar=$gShelfTopLevel')
		cmds.saveAllShelves(gShelfTopLevel)
	else:
		return