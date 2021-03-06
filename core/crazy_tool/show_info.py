
import bpy
import bmesh
import os
from bgl import *
import bpy
from bpy import context
from core.crazy_tool import export_obj

import numpy as np
import collections
import sys

from importlib import reload
reload(export_obj)

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


def show_info_3():
    print("--------show_info_3--------")
    pts_list = []
    scene = bpy.context.scene
    for obj in scene.objects:
        print("object name = ", obj.name)
        if "basel_mesh" in obj.name:

            scene.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            if obj.mode == 'EDIT':
                bm = bmesh.from_edit_mesh(obj.data)
                for v in bm.verts:
                    pt = np.array([v.co[0],v.co[1],v.co[2]])
                    pts_list.append(pt)

            bpy.ops.object.mode_set(mode='OBJECT')


def show_info_4():
    # fs bm.verts = 12021
    # bfm bm.verts = 53215

    print("--------show_info_4--------")
    scene = bpy.context.scene
    for obj in scene.objects:

        if "basel_mesh" in obj.name:
            scene.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            if obj.mode == 'EDIT':
                bm = bmesh.from_edit_mesh(obj.data)
                print("bfm bm.verts = ", len(bm.verts))

            bpy.ops.object.mode_set(mode='OBJECT')

        if "base_shape" in obj.name:
            scene.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            if obj.mode == 'EDIT':
                bm = bmesh.from_edit_mesh(obj.data)
                print("fs bm.verts = ", len(bm.verts))

            bpy.ops.object.mode_set(mode='OBJECT')

def show_info_5():
    print("--------show_info_4--------")
    scene = bpy.context.scene
    for obj in scene.objects:
        if "006_顔" in obj.name:
            mesh = obj.to_mesh
            print("dir of mesh = ",dir(mesh))




def show_info_6():

    # print all objects
    for obj in bpy.data.objects:
        print("object  = ", obj.name)

    for mesh in bpy.data.meshes:
        print(" mesh name = ", mesh.name)
        obj_loc = bpy.data.objects['basel_mesh'].location
        print("obj_loc =",obj_loc)

        for v in mesh.vertices:
            pt = np.array([v.co[0],v.co[1],v.co[2]])
            print("pt =",pt)
            break


def show_info_7_uv():

    root_path="OBJ"
    export_obj.export(root_path,"mesh.obj","mesh")











def show_blendshape():
    # print("--------show_blendshape--------")

    save_root_path="./"

    scene = bpy.context.scene
    for obj in scene.objects:
        if hasattr(obj.data,"shape_keys"):
            if hasattr(obj.data.shape_keys, "key_blocks"):

                scene.objects.active = obj
                bpy.ops.object.mode_set(mode='EDIT')
                if obj.mode == 'EDIT':
                    bm = bmesh.from_edit_mesh(obj.data)
                    print(obj.name, " bm.verts = ", len(bm.verts))
                bpy.ops.object.mode_set(mode='OBJECT')


                blendshapes = obj.data.shape_keys.key_blocks
                blendshapes_dict = collections.OrderedDict()
                for key in blendshapes.keys():
                    pts_list=[]
                    for v in blendshapes[key].data:
                        pt = np.array([v.co[0], v.co[1], v.co[2]])
                        pts_list.append(pt)
                    blendshapes_dict[key] = np.array(pts_list)


                for key in blendshapes_dict.keys():
                    print(key,blendshapes_dict[key].shape)



                    save_path = os.path.join(save_root_path,obj.name)
                    if os.path.exists(save_path) == False:
                        os.mkdir(save_path)
                    save_basis_file = os.path.join(save_path,key+".txt")
                    basis = blendshapes_dict[key]
                    np.savetxt(save_basis_file,basis)

def ReplaceName():

    scene = bpy.context.scene
    for obj in scene.objects:
        # print("obj mmd_rigid =",obj.mmd_rigid.name)

        if obj.mmd_joint.name is not "":
            print("obj mmd_joint =", obj.mmd_joint.name)
        elif obj.mmd_rigid.name is not "":
            print("obj mmd_rigid =", obj.mmd_rigid.name)
        else:
            print("obj name = ", obj.name)
            print("obj mmd_joint =", obj.mmd_joint.name)




            # for x in bpy.context.object.data.bones:
    #     print("name = ",x.name)
    #     x.name = x.name.replace('全ての親', 'root')
    #     x.name = x.name.replace('つま先ＩＫ', 'ik_ball')
    #     x.name = x.name.replace('足ＩＫ', 'ik_foot')
    #     x.name = x.name.replace('足首先', 'ball')
    #     x.name = x.name.replace('足首', 'foot')
    #     x.name = x.name.replace('足', 'thigh')
    #     x.name = x.name.replace('センター', 'spine_01')
    #     x.name = x.name.replace('下半身', 'pelvis')
    #     x.name = x.name.replace('ひざ', 'calf')
    #     x.name = x.name.replace('上半身２', 'spine_03')
    #     x.name = x.name.replace('上半身', 'spine_02')
    #     x.name = x.name.replace('肩', 'clavicle')
    #     x.name = x.name.replace('腕捩', 'upperarm_twist_01')
    #     x.name = x.name.replace('腕', 'upperarm')
    #     x.name = x.name.replace('ひじ', 'lowerarm')
    #     x.name = x.name.replace('手捩', 'lowerarm_twist_01')
    #     x.name = x.name.replace('手首', 'hand')
    #     x.name = x.name.replace('親指０', 'thumb_01')
    #     x.name = x.name.replace('親指１', 'thumb_02')
    #     x.name = x.name.replace('親指２', 'thumb_03')
    #     x.name = x.name.replace('小指', 'pinky')
    #     x.name = x.name.replace('薬指', 'ring')
    #     x.name = x.name.replace('中指', 'middle')
    #     x.name = x.name.replace('人指', 'index')
    #     x.name = x.name.replace('首', 'neck_01')
    #     x.name = x.name.replace('頭', 'head')
    #     x.name = x.name.replace('スカート', 'skirt')
    #     x.name = x.name.replace('髪', 'hair')
    #     x.name = x.name.replace('両目', 'eyes')
    #     x.name = x.name.replace('目', 'eye')
    #     x.name = x.name.replace('横', 'side')
    #     x.name = x.name.replace('側', 'side')
    #     x.name = x.name.replace('後ろ', 'back')
    #     x.name = x.name.replace('後', 'back')
    #     x.name = x.name.replace('前', 'front')
    #     x.name = x.name.replace('１', '_01')
    #     x.name = x.name.replace('２', '_02')
    #     x.name = x.name.replace('３', '_03')
    #     x.name = x.name.replace('４', '_04')
    #     x.name = x.name.replace('５', '_05')
    #     x.name = x.name.replace('６', '_06')
    #     x.name = x.name.replace('７', '_07')
    #     x.name = x.name.replace('８', '_08')
    #     x.name = x.name.replace('９', '_09')
    #     x.name = x.name.replace('.R', '_r')
    #     x.name = x.name.replace('.L', '_l')


def Output_vetices_index(file):
    obj = bpy.context.object;
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        with open(file, "w") as f:
            # f.write('Selected vertices index =' + '\r')
            # cnt=0
            for v in bm.verts:
                if v.select:
                    print("v.index=",v.index)
                    f.write(str(v.index)+'\r')
                    #         cnt =cnt + 1
                    # print("all selected vertices num="+str(cnt))
def Output_faces_index(file):
    obj = bpy.context.object;
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        with open(file, "w") as file:
            # f.write('Selected vertices index =' + '\r')
            # cnt=0
            for f in bm.faces:
                if f.select:
                    file.write(str(f.index)+'\r')

def Intput_vetices_index(file):
    obj = bpy.context.object
    file = open(file, 'r')
    lines = file.readlines()
    for i in range(0,len(lines),1):
        lines[i] = int(lines[i].replace('\n',''))
    indexs=np.array(lines)
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        for i in range(0,indexs.shape[0],1):
            bm.verts[indexs[i]].select = True

def Intput_faces_index(file):
    obj = bpy.context.object
    file = open(file, 'r')
    lines = file.readlines()
    for i in range(0,len(lines),1):
        lines[i] = int(lines[i].replace('\n',''))
    indexs=np.array(lines)
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        for i in range(0,indexs.shape[0],1):
            bm.faces[indexs[i]].select = True


def GetMeshIDS():



    face_file = "./icp_face_part.txt"

    # Intput_vetices_index(vertices_file)
    # Output_vetices_index(vertices_file)

    # Intput_faces_index(face_file)
    Output_faces_index(face_file)



def main():
    show_info_7_uv()

    pass





