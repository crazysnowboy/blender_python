from importlib import reload
from core import Manager

reload(Manager)

if __name__ == "__main__":
    Manager.register()
    # Manager.unregister()

    print("good boy")



