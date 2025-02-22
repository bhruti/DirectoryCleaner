import os
import shutil

cwd=os.getcwd()
all_files=os.listdir()
d={"folder":[]}
for path in all_files:
    if(path == "clean.py" or path=="folder"):
        continue
    if os.path.isfile(path):
        extension = path[path.rfind(".")+1:]
        if extension in d:
            d[extension].append(path)
        else:
            d[extension]=[path]
    elif os.path.isdir(path):
        d['folder'].append(path)

errors={}
for i in d:
    os.makedirs(i, exist_ok=True)
    for j in d[i]:
        # print(os.path.join(cwd,i,j))
        try:
            shutil.move(j, os.path.join(cwd,i,j))
        except Exception as e:
            errors[j]=str(e)  # Store error details instead of stopping the loop

if(len(errors) >0 ):
    print("\nErrors encountered:")
    for err in errors:
        print(err)
        print(errors[err])