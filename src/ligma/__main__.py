import os
import sys
import types
import importlib.util

__version__ = '0.1.1'

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

shell = import_module(f'{os.path.dirname(os.path.abspath(__file__))}{os.sep}shell.py')

args = sys.argv
args.pop(0)

if not len(args):
    shell.main(__version__)
elif len(args) == 1:
    print("Script parsing soon...")
else:
    print("Currently not supported!")
