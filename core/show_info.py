
import bpy
import bmesh

def show_info_1():
    print("--------crazy_show_info--------")

    # print all objects
    for obj in bpy.data.objects:
        print("object  = ", obj.name)

    for mesh in bpy.data.meshes:
        print(" mesh name = ", mesh.name)

        # for v in mesh.vertices:
        #     pt = np.array([v.co[0],v.co[1],v.co[2]])
        #     print("pt =",pt)

    obj = bpy.context.object
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        for f in bm.faces:
            if f.select:
                print("selected f index=", f.index)

        for v in bm.verts:
            if v.select:
                print("selected v.index=", v.index)

        for f in bm.faces:
            for v in f.verts:
                print("f[" + str(f.index) + "] id = ", v.index)
            print(" f material_index = ", f.material_index)
            break

        for v in bm.verts:
            print(" v =", v.co)
            break

        # for i in range(0, indexs.shape[0], 1):
        #     bm.faces[indexs[i]].select = True


def show_info_2():
    print("--------show_info_2--------")

    scene = bpy.context.scene
    for obj in scene.objects:
        print("object name = ", obj.name)
        if "basel_mesh" in obj.name:

            scene.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            if obj.mode == 'EDIT':
                bm = bmesh.from_edit_mesh(obj.data)
                for v in bm.verts:
                    print(" v =", v.co)
                    # v.co[0]=0
                    # v.co[1]=0
                    # v.co[2]=0
                    break


            bpy.ops.object.mode_set(mode='OBJECT')
