from  argparse import ArgumentParser

def BlenderRun():
    from core import Manager
    from importlib import reload
    reload(Manager)

    Manager.register()
    # Manager.unregister()

def LocalRun():
    print("good boy")




if __name__ == "__main__":
    parse = ArgumentParser()
    parse.add_argument("-m", type=str,default="blender")
    args = parse.parse_args()
    if args.m=="blender":
        BlenderRun()
    else:
        LocalRun()
    print("--------running-------------")



