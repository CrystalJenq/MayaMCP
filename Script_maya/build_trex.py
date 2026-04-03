"""
Build a T-Rex model in Maya using polygon primitives.
Run this via run_maya_script_from_vsc.py or directly in Maya Script Editor.
"""
import maya.cmds as cmds

def build_trex():
    # Clear selection
    cmds.select(clear=True)
    parts = []

    def make_box(name, tx=0, ty=0, tz=0, sx=1, sy=1, sz=1, rx=0, ry=0, rz=0):
        obj = cmds.polyCube(name=name, w=sx, h=sy, d=sz, sx=2, sy=2, sz=2)[0]
        cmds.move(tx, ty, tz, obj)
        if rx or ry or rz:
            cmds.rotate(rx, ry, rz, obj)
        parts.append(obj)
        return obj

    def make_cyl(name, tx=0, ty=0, tz=0, sx=1, sy=1, sz=1, rx=0, ry=0, rz=0, caps=1):
        obj = cmds.polyCylinder(name=name, r=sx, h=sy, sc=caps, ax=(0,1,0))[0]
        cmds.scale(1, 1, sz/sx if sx != 0 else 1, obj, r=True)
        cmds.move(tx, ty, tz, obj)
        if rx or ry or rz:
            cmds.rotate(rx, ry, rz, obj)
        parts.append(obj)
        return obj

    def make_sphere(name, tx=0, ty=0, tz=0, r=1):
        obj = cmds.polySphere(name=name, r=r)[0]
        cmds.move(tx, ty, tz, obj)
        parts.append(obj)
        return obj

    # --- BODY ---
    make_box("trex_body",       tx=0,   ty=5.0,  tz=0,    sx=3.2, sy=2.4, sz=4.5)
    make_box("trex_chest",      tx=0,   ty=5.3,  tz=2.0,  sx=2.6, sy=1.8, sz=1.8)
    make_box("trex_hips",       tx=0,   ty=4.2,  tz=-1.2, sx=2.4, sy=1.6, sz=2.0)

    # --- NECK ---
    make_box("trex_neck",       tx=0,   ty=6.3,  tz=1.8,  sx=1.2, sy=2.0, sz=1.2, rx=-30)

    # --- HEAD ---
    make_box("trex_skull",      tx=0,   ty=7.8,  tz=3.2,  sx=2.2, sy=1.6, sz=3.0)
    make_box("trex_snout",      tx=0,   ty=7.4,  tz=4.8,  sx=1.6, sy=1.0, sz=2.0)
    make_box("trex_jaw",        tx=0,   ty=6.7,  tz=3.8,  sx=1.8, sy=0.5, sz=2.8)
    make_box("trex_jaw_tip",    tx=0,   ty=6.5,  tz=5.0,  sx=1.2, sy=0.4, sz=1.4)

    # Eye sockets
    make_sphere("trex_eye_L",   tx=-0.9, ty=8.2, tz=2.6,  r=0.28)
    make_sphere("trex_eye_R",   tx= 0.9, ty=8.2, tz=2.6,  r=0.28)

    # --- TAIL ---
    make_box("trex_tail1",  tx=0, ty=4.8, tz=-3.2, sx=2.0, sy=1.6, sz=2.2, rx= 8)
    make_box("trex_tail2",  tx=0, ty=4.0, tz=-5.2, sx=1.4, sy=1.2, sz=2.0, rx=18)
    make_box("trex_tail3",  tx=0, ty=3.0, tz=-7.0, sx=0.9, sy=0.9, sz=1.8, rx=28)
    make_box("trex_tail4",  tx=0, ty=1.9, tz=-8.5, sx=0.5, sy=0.5, sz=1.6, rx=38)
    make_box("trex_tail5",  tx=0, ty=1.0, tz=-9.6, sx=0.3, sy=0.3, sz=1.2, rx=45)

    # --- ARMS (tiny T-Rex arms) ---
    for side, sign in [("L", -1), ("R", 1)]:
        x = sign * 1.7
        make_box(f"trex_upper_arm_{side}", tx=x, ty=5.6, tz=2.2, sx=0.45, sy=0.9, sz=0.45, rx=20, rz=sign*-15)
        make_box(f"trex_lower_arm_{side}", tx=x*1.05, ty=4.9, tz=2.7, sx=0.35, sy=0.8, sz=0.35, rx=40)
        make_box(f"trex_hand_{side}",      tx=x*1.08, ty=4.3, tz=3.1, sx=0.3,  sy=0.3, sz=0.5)
        # claws
        for ci, cz in enumerate([3.4, 3.6]):
            make_box(f"trex_claw_{side}_{ci}", tx=x*1.1 + ci*sign*0.08, ty=4.1, tz=cz, sx=0.08, sy=0.08, sz=0.35, rx=30)

    # --- LEGS ---
    for side, sign in [("L", -1), ("R", 1)]:
        x = sign * 1.1
        # thigh
        make_box(f"trex_thigh_{side}",  tx=x, ty=3.0, tz=0.3,  sx=1.0, sy=2.2, sz=1.0, rx=-10, rz=sign*5)
        # shin
        make_box(f"trex_shin_{side}",   tx=x*1.1, ty=1.2, tz=0.9,  sx=0.8, sy=2.0, sz=0.8, rx=20)
        # ankle
        make_box(f"trex_ankle_{side}",  tx=x*1.15, ty=0.3, tz=1.4,  sx=0.7, sy=0.6, sz=0.7)
        # foot pad
        make_box(f"trex_foot_{side}",   tx=x*1.2, ty=0.05, tz=1.8,  sx=0.9, sy=0.2, sz=2.0)
        # three toes
        for ti, (tz_off, tx_off) in enumerate([(-0.1, 0), (0.1, -0.25), (0.1, 0.25)]):
            make_box(f"trex_toe_{side}_{ti}",
                     tx=x*1.2 + tx_off, ty=0.06, tz=2.8 + tz_off,
                     sx=0.22, sy=0.18, sz=0.8)
            make_box(f"trex_toe_claw_{side}_{ti}",
                     tx=x*1.2 + tx_off, ty=0.0, tz=3.25 + tz_off,
                     sx=0.12, sy=0.12, sz=0.3, rx=15)

    # --- GROUP ALL ---
    grp = cmds.group(parts, name="T_Rex_GRP")
    # Centre pivot to bounding box
    cmds.xform(grp, centerPivots=True)
    # Move so feet sit on Y=0
    bb = cmds.exactWorldBoundingBox(grp)
    cmds.move(0, -bb[1], 0, grp, relative=True)

    # Basic grey material
    mat = cmds.shadingNode("lambert", asShader=True, name="trex_skin_MAT")
    cmds.setAttr(mat + ".color", 0.25, 0.30, 0.18, type="double3")  # dark olive green
    sg  = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name="trex_skin_SG")
    cmds.connectAttr(mat + ".outColor", sg + ".surfaceShader", force=True)
    cmds.sets(grp, edit=True, forceElement=sg)

    cmds.select(grp)
    print(f"T-Rex built! Group: '{grp}'  ({len(parts)} parts)")
    return grp

build_trex()
