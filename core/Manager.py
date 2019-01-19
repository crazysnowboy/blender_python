import bpy
from importlib import reload
from core.crazy_tool import BlenderUI
from core  import mmd_tools
reload(BlenderUI)
reload(BlenderUI)

def register():
    print("---register---HelloWorldPanel------")

    # mmd_tools.register()
    bpy.utils.register_class(BlenderUI.ShowInfo)
    bpy.utils.register_class(BlenderUI.DeleteObjects)
    bpy.utils.register_class(BlenderUI.LoadObj)
    bpy.utils.register_class(BlenderUI.CrazyTools)


def unregister():

    print("--unregister----HelloWorldPanel------")

    mmd_tools.unregister()
    bpy.utils.unregister_class(BlenderUI.ShowInfo)
    bpy.utils.unregister_class(BlenderUI.DeleteObjects)
    bpy.utils.unregister_class(BlenderUI.LoadObj)
    bpy.utils.unregister_class(BlenderUI.CrazyTools)

