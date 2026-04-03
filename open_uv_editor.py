import maya.cmds as cmds
import maya.mel as mel

def open_uv_editor():
    """
    Opens the Maya UV Editor window.
    """
    try:
        # Check if the UV Editor window already exists
        if cmds.window("polyTexturePlacementPanel1Window", exists=True):
            # If it exists, just show/raise the window
            cmds.showWindow("polyTexturePlacementPanel1Window")
            print("UV Editor window brought to front.")
        else:
            # If it doesn't exist, call the standard creation command
            mel.eval('TextureViewWindow;')
            print("UV Editor created and opened.")
    except Exception as e:
        print(f"Error opening UV Editor: {e}")

# Call directly to ensure execution when sent via socket
open_uv_editor()