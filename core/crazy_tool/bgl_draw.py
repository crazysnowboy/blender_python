import bpy
import bgl
import blf
import bmesh
import numpy as np
from core import tools
import mathutils
import copy
handles_list = []
select_points=[]

def draw_line_3d(color, start, end, width=1):
    bgl.glLineWidth(width)
    bgl.glColor4f(*color)
    bgl.glBegin(bgl.GL_LINES)
    bgl.glVertex3f(*start)
    bgl.glVertex3f(*end)


def draw_callback_3d(self, context,ids1,ids2):



    basel_pts_list = []
    base_pts_list = []
    basel_scale=10.0

    for mesh in bpy.data.meshes:
        if "mesh1" in mesh.name:
            obj_loc = bpy.data.objects['basel_mesh'].location
            for bfm_i in ids1:
                v = mesh.vertices[bfm_i]
                pt = np.array([v.co[0],v.co[2],v.co[1]])*basel_scale
                pt_b = np.array([obj_loc[0],obj_loc[1],obj_loc[2]])
                basel_pts_list.append(pt+pt_b)
        if "mesh2" in mesh.name:
            obj_loc = bpy.data.objects['base_shape'].location

            for fs_i in ids2:
                v = mesh.vertices[fs_i]
                pt = np.array([v.co[0],-v.co[2],v.co[1]])
                pt_b = np.array([obj_loc[0],obj_loc[1],obj_loc[2]])
                base_pts_list.append(pt+pt_b)

    basel_vertices = np.array(basel_pts_list)
    fs_vertices = np.array(base_pts_list)

    bgl.glEnable(bgl.GL_BLEND)
    for i in range(0,fs_vertices.shape[0]):
        pt = fs_vertices[i,:]
        v1 = mathutils.Vector((pt[0], pt[1], pt[2]))
        pt = basel_vertices[i,:]
        v2 = mathutils.Vector((pt[0], pt[1], pt[2]))
        draw_line_3d((0.0, 1.0, 0.0, 0.7), v1, v2)
    bgl.glEnd()
    # restore opengl defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)



class draw_class(bpy.types.Operator):

    bl_idname = "mesh.draw_class"
    bl_label = "draw_class"
    bl_options = {"UNDO"}

    def invoke(self, context, event) :
        if context.area.type == 'VIEW_3D':

            args = (self, context)
            handle_3d = bpy.types.SpaceView3D.draw_handler_add(draw_callback_3d, args, 'WINDOW', 'POST_VIEW')
            handles_list.append(handle_3d)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}


class bgl_clear_class(bpy.types.Operator):

    bl_idname = "mesh.bgl_clear_class"
    bl_label = "bgl_clear_class"
    bl_options = {"UNDO"}

    def invoke(self, context, event):
        for h in handles_list:
            bpy.types.SpaceView3D.draw_handler_remove(h, 'WINDOW')
        handles_list.clear()

        return {'FINISHED'}

class select_points_class(bpy.types.Operator):

    bl_idname = "mesh.select_points_class"
    bl_label = "select_points_class"
    bl_options = {"UNDO"}

    def invoke(self, context, event):
        select_points.clear()
        obj = bpy.context.object;
        if obj.mode == 'EDIT':
            bm = bmesh.from_edit_mesh(obj.data)
            for v in bm.verts:
                if v.select:
                    select_points.append(v.index)
                    print(v.index)


        return {'FINISHED'}



class bgl_Draw(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category="crazy_tools"

    bl_idname = "bgl_Draw"
    bl_label = "Hello bgl_Draw"


    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("mesh.draw_class", text = "bgl_draw")

        row = layout.row()
        row.operator("mesh.bgl_clear_class", text = "clear_bgl")

        row = layout.row()
        row.operator("mesh.select_points_class", text = "select_points")

def register():

    bpy.utils.register_class(select_points_class)

    bpy.utils.register_class(draw_class)

    bpy.utils.register_class(bgl_clear_class)
    bpy.utils.register_class(bgl_Draw)


def unregister():
    bpy.utils.unregister_class(select_points_class)

    bpy.utils.unregister_class(draw_class)
    bpy.utils.unregister_class(bgl_clear_class)

    bpy.utils.unregister_class(bgl_Draw)

