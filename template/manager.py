import sys
import os
import keyboard
import shutil

def check(x, text):
    if not exists(x):
        print('' + text)
        exit()

def exists(i):
    if i >= len(sys.argv):
        return False
    return True

if not exists(1):
    print("\033[91mFailed: Please specify a command.\033[0m")
elif sys.argv[1] == "ent":
    check(2, "\033[91mFailed: Please specify an entity name.\033[0m")
    shutil.copy("./entities/template.py", f"./entities/e_{sys.argv[2]}.py")
    with open("./entities/entities.py", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(f"from entities.e_{sys.argv[2]} import {sys.argv[2].capitalize()}\n" + content)

    with open(f"./entities/e_{sys.argv[2].capitalize()}.py", 'r+') as f:
        content = f.read()
        new_content = content.replace("template", sys.argv[2].capitalize())
        f.seek(0)
        f.write(new_content)
        f.truncate()

    print("\033[92mSuccess: Created new entity named {sys.argv[2]}\033[0m")

elif sys.argv[1] == "run":
    os.system('cmd /c "python main.py"')

elif sys.argv[1] == "new":
    check(2, "\033[91mFailed: Please specify a project name.\033[0m")
    try:
        shutil.copytree('./compiled', sys.argv[2])
    except FileExistsError:
        print(f"\033[91mFailed: Please make sure that folder ./{sys.argv[2]} doesn't exist already. If it doesn't, please retry after a few seconds.\033[0m")
        exit()
    except Exception as e:
        print("\033[91mFailed: An unexpected error occurred while copying project files. Press s to show the error, press any other key to exit.\033[0m")
        key = keyboard.read_event().name
        if key == 's':
            print(e)
            exit()
            
    print(f'\033[92mSuccess: Created project named "{sys.argv[2]}".\033[0m\nTo continue, we recommend the following commands:\n\033[90m  >> cd {sys.argv[2]}\n  >> us run\n\n\033[0mGood Luck!\033[0m')