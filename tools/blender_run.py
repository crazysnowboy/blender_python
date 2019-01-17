import bpy
import os
import sys


paths=['']
project_root=""
file_name = "blender_script.py"



for path in paths:
    sys.path.append(path)

py_file_name = os.path.join(project_root, file_name)
exec(compile(open(py_file_name).read(), py_file_name, 'exec'))