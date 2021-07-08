import os
import sys
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

class EasterEggs:
    def __init__(self):
        self.rickroll = """
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
        """

EasterEggs = EasterEggs()

core = import_module(f'{os.path.dirname(os.path.abspath(__file__))}{os.sep}core.py')

def main(version):
    print(f"Ligma {version}")
    while True:
        try:
            userinput = input("ligma > ")
        except KeyboardInterrupt:
            print()
            print(core.KeyboardStop().as_string())
            continue
        if userinput == "exit" or userinput == "quit":
            sys.exit()
        elif userinput == "nuts" or userinput == "balls":
            print()
            print(EasterEggs.rickroll)
            continue
        result, error = core.run(userinput)
        if error: print(error.as_string())
        else: print(result)
