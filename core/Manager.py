import bpy
from importlib import reload
from core.crazy_tool import BlenderUI
from core  import mmd_tools
from core.crazy_tool import bgl_draw
from core.crazy_tool import uv_editor
from core import UvSquares
reload(BlenderUI)
reload(bgl_draw)

def register():
    print("---register---HelloWorldPanel------")

    # mmd_tools.register()
    # bgl_draw.register()
    # UvSquares.register()
    # uv_editor.register()

    bpy.utils.register_class(BlenderUI.ShowInfo)
    bpy.utils.register_class(BlenderUI.DeleteObjects)
    bpy.utils.register_class(BlenderUI.LoadObj)
    bpy.utils.register_class(BlenderUI.CrazyTools)


def unregister():

    print("--unregister----HelloWorldPanel------")

    # mmd_tools.unregister()
    bgl_draw.unregister()
    UvSquares.unregister()

    # uv_editor.unregister()


    bpy.utils.unregister_class(BlenderUI.ShowInfo)
    bpy.utils.unregister_class(BlenderUI.DeleteObjects)
    bpy.utils.unregister_class(BlenderUI.LoadObj)
    bpy.utils.unregister_class(BlenderUI.CrazyTools)

