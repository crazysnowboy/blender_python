import sys
import os

def blender_run():
    import bpy
    paths=['']
    project_root=""
    file_name = "blender_script.py"

    for path in paths:
        sys.path.append(path)

    py_file_name = os.path.join(project_root, file_name)
    exec(compile(open(py_file_name).read(), py_file_name, 'exec'))

def get_paths():
    print(sys.path)


if __name__ == "__main__":
    # get_paths()
    blender_run()