import maya.cmds as cmds

def list_scene_outliner_info():
    """
    Retrieves and prints the hierarchy of the current Maya scene,
    including object names, types, and visibility status.
    """
    # Get all top-level nodes (assemblies) in the scene
    assemblies = cmds.ls(assemblies=True, long=True)
    
    if not assemblies:
        print("The scene is currently empty.")
        return

    print("\n" + "="*80)
    print(f"{'Hierarchy (Object Name)':<50} | {'Node Type':<15} | {'Hidden'}")
    print("-" * 80)

    def walk_hierarchy(nodes, depth=0):
        for node in nodes:
            # Get the short name for display and the long name for queries
            short_name = node.split('|')[-1]
            node_type = cmds.nodeType(node)
            
            # Check visibility attribute
            is_hidden = not cmds.getAttr(f"{node}.visibility")
            
            # Format the output with indentation
            indent = "  " * depth
            print(f"{indent + short_name:<50} | {node_type:<15} | {is_hidden}")
            
            # Find children (only transforms to keep the list clean, like the default Outliner)
            children = cmds.listRelatives(node, children=True, type='transform', fullPath=True)
            if children:
                walk_hierarchy(children, depth + 1)

    walk_hierarchy(assemblies)
    print("="*80 + "\n")

# Call directly to ensure execution when sent via socket
list_scene_outliner_info()