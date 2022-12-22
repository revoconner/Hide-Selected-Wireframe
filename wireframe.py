import maya.cmds as cmds
state = cmds.displayPref(q=True, wsa=True)
if (state == "none"): state="full"
else: state="none"
cmds.displayPref(wsa=state)
