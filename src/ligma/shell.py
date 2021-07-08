import os
import types
import importlib

def import_module(module_path: str) -> types.ModuleType:
    """
    Return a module class from given file path.

    Arguments:
    `module_path: str` Path to .py file.
    """
    filename = os.path.basename(os.path.realpath(module_path))
    spec = importlib.util.spec_from_file_location(filename, module_path)
    module_obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module_obj)
    return module_obj

core = import_module(f'{os.path.dirname(os.path.abspath(__file__))}{os.sep}core.py')

def main(version):
    print(f"Ligma {version}")
    while True:
        userinput = input("ligma > ")
        result, error = core.run(userinput)
        if error: print(error.as_string())
        else: print(result)
