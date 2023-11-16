import sys
import shutil
import os

def check(x, text):
    if not exists(x):
        print(text)
        
def exists(i):
    if i >= len(sys.argv):
        return False
    return True

if not exists(1):
    print("please specify a command.")
elif sys.argv[1] == "ent":
    check(2, "Please specify an entity name.")
    shutil.copy("./entities/template.py", f"./entities/e_{sys.argv[2]}.py")
    with open("./entities/entities.py", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(f"from entities.e_{sys.argv[2]} import {sys.argv[2]}\n" + content)
    
    with open(f"./entities/e_{sys.argv[2]}.py", 'r+') as f:
        content = f.read()
        new_content = content.replace("template", sys.argv[2])
        f.seek(0)
        f.write(new_content)
        f.truncate()

elif sys.argv[1] == "run":
    os.system('cmd /c "python main.py"')