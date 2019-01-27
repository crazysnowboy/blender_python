import bpy
from core.crazy_tool import import_obj, show_info
from importlib import reload
from bpy_extras import io_utils
from mathutils import Matrix

reload(import_obj)
reload(show_info)

global_scale = 1.0


class LoadObj(bpy.types.Operator):

    bl_idname = "mesh.crazy_load_obj"
    bl_label = "crazy_load_obj"
    bl_options = {"UNDO"}

    def Test(self,context):


        basel_model_path = "_mesh.obj"


        global_matrix = io_utils.axis_conversion(to_forward="Z",
                                                 to_up="-Y",
                                                 ).to_4x4() * Matrix.Scale(global_scale, 4)

        import_obj.load(context, basel_model_path, global_matrix=global_matrix)




        # basel_model_path = "mesh.obj"
        # import_obj.load(context, basel_model_path)

    def invoke(self, context, event) :

        self.Test(context)

        return {"FINISHED"}

class DeleteObjects(bpy.types.Operator):

    bl_idname = "mesh.crazy_all_delete_objects"
    bl_label = "crazy_all_delete_objects"
    bl_options = {"UNDO"}
    def invoke(self, context, event) :
        print("--------delete all objects---------")

        # # remove mesh Cube
        for mesh in bpy.data.meshes:
            print("delete mesh = ",mesh)
            bpy.data.meshes.remove(mesh)

        return {"FINISHED"}


class ShowInfo(bpy.types.Operator):

    bl_idname = "mesh.crazy_show_info"
    bl_label = "crazy_show_info"
    bl_options = {"UNDO"}
    def invoke(self, context, event) :
        # show_info.show_info_1()
        # show_info.show_info_4()
        # show_info.ReplaceName()
        # show_info.show_blendshape()
        show_info.main()


        return {"FINISHED"}


class CrazyTools(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    bl_idname = "VIEW3D_PT_test"
    bl_label = "Hello World Panel"
    bl_category="crazy_tools"


    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')


        row = layout.row()
        row.operator("mesh.crazy_show_info", text = "show_info")


        row = layout.row()
        row.operator("mesh.crazy_load_obj", text = "load_obj")

        row = layout.row()
        row.operator("mesh.crazy_all_delete_objects", text = "delete_all_objects")