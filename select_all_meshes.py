import maya.cmds as cmds

def select_all_meshes():
    """
    Selects the transform nodes of all polygon meshes in the scene.
    """
    # 1. Ensure we are in Object Selection Mode
    cmds.selectMode(object=True)

    # 2. Find all mesh shape nodes (excluding intermediate/history nodes)
    mesh_shapes = cmds.ls(type='mesh', noIntermediate=True, long=True)

    if not mesh_shapes:
        print("No mesh objects found in the scene.")
        return

    # 3. Get the parent transform nodes
    # Using 'or []' handles cases where listRelatives might return None
    parents = cmds.listRelatives(mesh_shapes, parent=True, fullPath=True) or []
    unique_transforms = list(set(parents))

    if unique_transforms:
        # 4. Perform selection
        cmds.select(unique_transforms, replace=True)
        
        # 5. Force the viewport to update so you can see the selection
        cmds.refresh()
        print(f"Successfully selected {len(unique_transforms)} mesh objects.")
    else:
        print("Found mesh shapes, but they have no valid transform parents.")

# Call directly to ensure execution when sent via socket
select_all_meshes()