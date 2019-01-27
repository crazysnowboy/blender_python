
import os
import bpy
import numpy as np
from bpy import context
import bmesh

def WriteOBJ(root_path, file_name, vertexs, vertex_normals =0,triangles=0, texture_coordinate=0, vertex_color=0, tri_index_offset=0):
    obj_file_path=os.path.join(root_path,file_name)

    print("write obj = ", obj_file_path)
    c_i = 0  # vertex color index

    with open(obj_file_path, 'w') as test_txt:

        test_txt.write("mtllib basel_mesh.mtl\n")
        if hasattr(texture_coordinate, 'shape'):

            for r in range(0, texture_coordinate.shape[0]):
                line = 'vt {} {}\n'.format(texture_coordinate[r, 0], texture_coordinate[r, 1])
                test_txt.write(line)
        if hasattr(vertexs, 'shape'):

            for r in range(0, vertexs.shape[0]):
                if hasattr(vertex_color, 'shape'):
                    # With RGBA
                    line = 'v {} {} {} {} {} {} {}\n'.format(vertexs[r, 0], vertexs[r, 1], vertexs[r, 2],
                                                             vertex_color[c_i, 0], vertex_color[c_i, 1],
                                                             vertex_color[c_i, 2], 255)
                    c_i = c_i + 1
                else:
                    # Without RGBA
                    line = 'v {} {} {}\n'.format(vertexs[r, 0], vertexs[r, 1], vertexs[r, 2])

                if hasattr(vertex_normals, 'shape'):
                    line = line + 'vn {} {} {}\n'.format(vertex_normals[r, 0], vertex_normals[r, 1], vertex_normals[r, 2])

                test_txt.write(line)
        if hasattr(triangles, 'shape'):
            test_txt.write("usemtl face\n")
            triangles = triangles.astype('int32')
            for r in range(0, triangles.shape[0]):
                triangles[r, :] = triangles[r, :] + tri_index_offset
                line = 'f {}/{} {}/{} {}/{}\n'.format(triangles[r, 0], triangles[r, 0],
                                                         triangles[r, 2], triangles[r, 2],
                                                         triangles[r, 1], triangles[r, 1])  # if with texture coordinate
                test_txt.write(line)


def export(obj_save_path,obj_name,mesh_name="basel_mesh"):


    vertex_list = []
    for mesh in bpy.data.meshes:
        if mesh_name in mesh.name:
            for v in mesh.vertices:
                pt = np.array([v.co[0],v.co[1],v.co[2]])
                vertex_list.append(pt)

    v = np.array(vertex_list)

    vertices_number = v.shape[0]
    faces_list=[]
    vertex_uvs = np.zeros((vertices_number,2),np.float32)
    vertex_normal = np.zeros((vertices_number,3),np.float32)

    scene = bpy.context.scene
    for obj in scene.objects:
        if mesh_name in obj.name:
            scene.objects.active = obj

            for idx,vertex in enumerate(obj.data.vertices):
                vertex_normal[idx,0] = vertex.normal[0]
                vertex_normal[idx,1] = vertex.normal[1]
                vertex_normal[idx,2] = vertex.normal[2]


            bpy.ops.object.mode_set(mode='EDIT')
            if obj.mode == 'EDIT':
                bm = bmesh.from_edit_mesh(obj.data)
                uv_layer = bm.loops.layers.uv.verify()
                bm.faces.layers.tex.verify()  # currently blender needs both layers.
                for f in bm.faces:
                    face_vetexs_list =[]
                    for l in f.loops:
                        # print(l.vert.index)
                        face_vetexs_list.append(l.vert.index)
                        luv = l[uv_layer]
                        x = float(luv.uv.x)
                        y = float(luv.uv.y)
                        vertex_uvs[l.vert.index,0]=x
                        vertex_uvs[l.vert.index,1]=y

                    f1 = face_vetexs_list[0]
                    f2 = face_vetexs_list[2]
                    f3 = face_vetexs_list[1]

                    faces_list.append(np.array([f1,f2,f3]))
            bpy.ops.object.mode_set(mode='OBJECT')





    f =np.array(faces_list)+1
    vt = vertex_uvs
    vn = vertex_normal


    print("f",f.shape)
    print("vt",vt.shape)
    print("v",v.shape)
    print("vn",vn.shape)



    WriteOBJ(obj_save_path,
                    obj_name,
                     vertexs=v,
                     vertex_normals =vn,
                     triangles=f,
                     texture_coordinate=vt,
                     vertex_color=0,
                     tri_index_offset=0)

