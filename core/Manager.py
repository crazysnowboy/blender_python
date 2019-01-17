import bpy
from importlib import reload
from core import BlenderUI

reload(BlenderUI)
reload(BlenderUI)

def register():
    print("---register---HelloWorldPanel------")
    bpy.utils.register_class(BlenderUI.ShowInfo)
    bpy.utils.register_class(BlenderUI.DeleteObjects)
    bpy.utils.register_class(BlenderUI.LoadObj)
    bpy.utils.register_class(BlenderUI.CrazyTools)


def unregister():

    print("--unregister----HelloWorldPanel------")
    bpy.utils.unregister_class(BlenderUI.ShowInfo)
    bpy.utils.unregister_class(BlenderUI.DeleteObjects)
    bpy.utils.unregister_class(BlenderUI.LoadObj)
    bpy.utils.unregister_class(BlenderUI.CrazyTools)

