import maya.cmds as cmds

def create_bus_v1(prefix="v1"):
    """
    Creates a basic bus model (Version 1).
    This serves as the base for future modifications.
    """
    # --- Parameters ---
    body_w = 12
    body_h = 4
    body_d = 4
    wheel_radius = 0.8
    
    # --- 1. Main Body ---
    # Create the primary cube for the bus chassis
    bus_body = cmds.polyCube(w=body_w, h=body_h, d=body_d, name=f'{prefix}_Bus_Body')[0]
    cmds.move(0, 2.5, 0, bus_body)

    # --- 2. Wheels ---
    # Define positions for 4 wheels
    wheel_positions = [
        (4, 0.8, 2.1), (4, 0.8, -2.1),   # Front
        (-4, 0.8, 2.1), (-4, 0.8, -2.1)  # Rear
    ]
    wheels = []
    for i, pos in enumerate(wheel_positions):
        w = cmds.polyCylinder(r=wheel_radius, h=0.6, sx=20, name=f'{prefix}_Wheel_{i+1}')[0]
        cmds.rotate(90, 0, 0, w)
        cmds.move(*pos, w)
        wheels.append(w)

    # --- 3. Windshield ---
    # Front glass panel
    windshield = cmds.polyCube(w=0.1, h=1.8, d=3.6, name=f'{prefix}_Windshield')[0]
    cmds.move(6.01, 3.3, 0, windshield)

    # --- 4. Side Windows ---
    # Create windows on both sides
    windows = []
    for side in [1, -1]:
        side_label = "L" if side == 1 else "R"
        for i in range(3):
            win = cmds.polyCube(w=2, h=1.4, d=0.1, name=f'{prefix}_Window_{side_label}_{i+1}')[0]
            cmds.move(-3.5 + (i * 2.8), 3.3, 2.01 * side, win)
            windows.append(win)

    # --- 5. Lights ---
    # Headlights
    headlight_L = cmds.polyCube(w=0.2, h=0.6, d=0.8, name=f'{prefix}_Headlight_L')[0]
    cmds.move(6.01, 1.8, 1.3, headlight_L)
    headlight_R = cmds.polyCube(w=0.2, h=0.6, d=0.8, name=f'{prefix}_Headlight_R')[0]
    cmds.move(6.01, 1.8, -1.3, headlight_R)

    # Taillights
    taillight_L = cmds.polyCube(w=0.2, h=0.4, d=1.0, name=f'{prefix}_Taillight_L')[0]
    cmds.move(-6.01, 1.8, 1.3, taillight_L)
    taillight_R = cmds.polyCube(w=0.2, h=0.4, d=1.0, name=f'{prefix}_Taillight_R')[0]
    cmds.move(-6.01, 1.8, -1.3, taillight_R)
    
    all_lights = [headlight_L, headlight_R, taillight_L, taillight_R]

    # --- 6. Refinement (Bevel) ---
    bevel_targets = [bus_body, windshield] + windows + all_lights
    for part in bevel_targets:
        if cmds.objExists(part):
            cmds.polyBevel(part, offset=0.15, segments=2, autoFit=True, roundness=1)

    # --- 7. Organization ---
    bus_group = cmds.group(bus_body, windshield, *wheels, *windows, *all_lights, name=f'{prefix}_Bus_GRP')

    # Clean history and center pivot
    cmds.delete(bus_group, ch=True)
    cmds.xform(bus_group, cp=True)

    print(f"Bus '{bus_group}' successfully built.")
    return bus_group

def create_porsche_v1(prefix="v1", offset_z=8):
    """
    Creates a simplified Porsche 911 style sports car (Version 1).
    Positioned next to the bus using offset_z.
    """
    # --- Parameters ---
    # Porsche is lower and wider than the bus
    body_w = 9
    body_h = 1.2
    body_d = 4.5
    wheel_radius = 0.7

    # --- 1. Main Body ---
    p_body = cmds.polyCube(w=body_w, h=body_h, d=body_d, name=f'{prefix}_Porsche_Body')[0]
    cmds.move(0, 0.8, offset_z, p_body)

    # --- 2. Cabin (Sleek sloped roof) ---
    p_cabin = cmds.polyCube(w=4.5, h=1.0, d=3.8, name=f'{prefix}_Porsche_Cabin')[0]
    cmds.move(-0.5, 1.9, offset_z, p_cabin)

    # --- 3. Spoiler (Iconic 911 feature) ---
    p_spoiler = cmds.polyCube(w=0.8, h=0.2, d=4.2, name=f'{prefix}_Porsche_Spoiler')[0]
    cmds.move(-4.6, 1.8, offset_z, p_spoiler)

    # --- 4. Wheels ---
    wheel_positions = [
        (3, 0.7, offset_z + 2.1), (3, 0.7, offset_z - 2.1),   # Front
        (-3, 0.7, offset_z + 2.1), (-3, 0.7, offset_z - 2.1)  # Rear
    ]
    wheels = []
    for i, pos in enumerate(wheel_positions):
        w = cmds.polyCylinder(r=wheel_radius, h=0.8, sx=20, name=f'{prefix}_P_Wheel_{i+1}')[0]
        cmds.rotate(90, 0, 0, w)
        cmds.move(*pos, w)
        wheels.append(w)

    # --- 5. Lights ---
    # Front Headlights (Oval style)
    h_light_L = cmds.polySphere(r=0.4, sx=10, sy=10, name=f'{prefix}_P_Headlight_L')[0]
    cmds.move(4.2, 1.2, offset_z + 1.4, h_light_L)
    cmds.scale(0.5, 1, 1, h_light_L)

    h_light_R = cmds.polySphere(r=0.4, sx=10, sy=10, name=f'{prefix}_P_Headlight_R')[0]
    cmds.move(4.2, 1.2, offset_z - 1.4, h_light_R)
    cmds.scale(0.5, 1, 1, h_light_R)

    # Rear Taillight strip
    t_light = cmds.polyCube(w=0.2, h=0.2, d=4.0, name=f'{prefix}_P_Taillight')[0]
    cmds.move(-4.51, 1.1, offset_z, t_light)
    
    all_parts = [p_body, p_cabin, p_spoiler, h_light_L, h_light_R, t_light]

    # --- 6. Refinement (Bevel) ---
    for part in all_parts:
        cmds.polyBevel(part, offset=0.1, segments=2, autoFit=True)

    # --- 7. Organization ---
    p_group = cmds.group(*all_parts, *wheels, name=f'{prefix}_Porsche_GRP')
    cmds.delete(p_group, ch=True)
    cmds.xform(p_group, cp=True)

    print(f"Porsche '{p_group}' successfully built.")
    return p_group

if __name__ == "__main__":
    # Cleanup existing groups
    for grp in ['v1_Bus_GRP', 'v1_Porsche_GRP']:
        if cmds.objExists(grp):
            cmds.delete(grp)
    
    # Create both vehicles
    bus_grp = create_bus_v1()
    create_porsche_v1(offset_z=8)

    # Select the bus group
    if bus_grp and cmds.objExists(bus_grp):
        cmds.select(bus_grp, replace=True)
        
        # Move the bus 2 units to the right (Positive X direction)
        cmds.move(2, 0, 0, bus_grp, relative=True)
        print(f"Selected target: {bus_grp} and moved it 2 units to the right.")

    cmds.viewFit()