def explore_module(module_name):
    """Use dir() to explore module attributes"""
    try:
        module = __import__(module_name)
        print(dir(module))
    except ModuleNotFoundError:
        print("Module not found!")
