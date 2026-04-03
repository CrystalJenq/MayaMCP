import maya.cmds as cmds

def select_all_mesh_faces():
    """
    Selects all faces of all polygon mesh objects in the scene.
    """
    # 1. Find all mesh shape nodes in the scene
    meshes = cmds.ls(type='mesh', noIntermediate=True, long=True)

    if not meshes:
        print("No mesh objects found in the scene.")
        return

    # 2. Optimization: Select mesh objects first, then convert to faces.
    # This is much faster than passing a massive list of component strings.
    cmds.select(meshes, replace=True)
    
    # 3. Convert selection to faces
    # This internal command is optimized for handling large amounts of components.
    cmds.ConvertSelectionToFaces()
    
    cmds.selectMode(component=True)
    cmds.selectType(polyFace=True)
    
    print(f"Successfully selected all faces of {len(meshes)} meshes.")

# Call directly to ensure execution when sent via socket
select_all_mesh_faces()