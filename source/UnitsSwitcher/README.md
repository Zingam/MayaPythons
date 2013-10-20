UnitsSwitcher
=============

Known issues:
-------------
 - Sometimes the shelf fails to properly initialize: try deleting it and unloading/reloading the plugin a few times.
 
TO DO:
-------------
Make a custom version in Python for "deleteShelfTab"


// Creation Date: 1996
//
//
//<doc>
//<name deleteShelfTab>
//
//<synopsis>
//		deleteShelfTab (string $shelfName) 
//
//<returns>
//		int :	1 = shelf tab was deleted
//				0 = if shelf tab not deleted
//
//<description>
//		Deletes a shelf layout and tab, and removes its preferences
//		so that it will not be loaded again.  The user is prompted
//		for confirmation of the delete.
//
//<flags>
//		string $shelfName Name of the shelf tab to delete
//
//<examples>
//  deleteShelfTab "Shelf2";
//
//</doc>

global proc int deleteShelfTab(string $shelfName) 
{
	int $returnStatus = 0;
	
	global string $gShelfForm;
	global string $gShelfTopLevel;

	setParent $gShelfTopLevel;
	string $shelves[] = `tabLayout -q -ca $gShelfTopLevel`;	
	int $numShelves = size($shelves);

	int $indexArr[];
	int $index = 0;
	int $nItems = 0;

	// Bail if there is something really weird going on
	if ($numShelves <= 0) return $returnStatus;
	
	// Check for the last shelf
	string $ok		= (uiRes("m_deleteShelfTab.kOK"));
	if (1 == $numShelves) {
		confirmDialog -title (uiRes("m_deleteShelfTab.kAlert"))  
			-button $ok 
			-defaultButton $ok 
			-message (uiRes("m_deleteShelfTab.kCannotDelete")) ;
		return $returnStatus;
	}

	// Confirm the delete
	if(!`exists shelfLabel_melToUI` ){
		source "shelfLabel.mel";
	}
	
	string $msg        = (uiRes("m_deleteShelfTab.kDeletionConfirmMsg"));
	string $shelfLabel = `shelfLabel_melToUI $shelfName`;
	string $dlgMsg     = `format -s $shelfLabel $msg`;  
	string $cancel     = (uiRes("m_deleteShelfTab.kCancel"));
	
	if ($cancel == `confirmDialog -title (uiRes("m_deleteShelfTab.kConfirm")) 
		-message $dlgMsg	-button $ok  -button $cancel -defaultButton $ok
		-cancelButton $cancel  -dismissString $cancel `) 
	{
		return $returnStatus;
	}

	// Okay, now we can delete the shelf tab
	
	int $i = 0;
	int $nShelves = 0;
	int $shelfNum = 0;

	//  update the preferences.
	//
	$nShelves = `optionVar -q numShelves`;
	for ($shelfNum = 1; $shelfNum <= $nShelves; $shelfNum++) {
		if ($shelfName == `optionVar -q ("shelfName" + $shelfNum)`) {
			break;
		}
	}
	for ($i = $shelfNum; $i <= $nShelves; $i++) {
		optionVar 
			-iv ("shelfLoad" + $i) `optionVar -q ("shelfLoad" + ($i+1))`
			-sv ("shelfName" + $i) `optionVar -q ("shelfName" + ($i+1))`
			-sv ("shelfFile" + $i) `optionVar -q ("shelfFile" + ($i+1))`;
	}
	optionVar -remove ("shelfLoad" + $nShelves)
		-remove ("shelfName" + $nShelves)
		-remove ("shelfFile" + $nShelves);
	$nShelves--;
	optionVar -iv numShelves $nShelves;

	// The optionVars have all been updated, so it's safe to delete and have
	// the shelfTabChange() method triggered. See Maya-3288.
	//
	deleteUI -layout ($gShelfTopLevel + "|" + $shelfName);
	
	string $shelfDirs = `internalVar -userShelfDir`;
	string $shelfArray[];
	string $PATH_SEPARATOR = `about -win`? ";" : ":";
	tokenize($shelfDirs, $PATH_SEPARATOR, $shelfArray);
	for( $i = 0; $i < size($shelfArray); $i++ ) {
		$fileName = ($shelfArray[$i] + "shelf_" + $shelfName + ".mel");
		string $deletedFileName = $fileName + ".deleted";

		//	Fix for bug #125494.  Remove the .deleted file if it already exists.
		//
		if (`filetest -r $deletedFileName`) {
			sysFile -delete $deletedFileName;
		}
	
		if (`file -q -exists $fileName`) {
			sysFile -rename $deletedFileName $fileName;
			break;
		}
	}
	
	//  Make sure the new active shelf tab has buttons.
	shelfTabChange();
				
	$returnStatus = 1;
	
	return $returnStatus;
}
 
 