import os

directory="learning_scripting"
parent_dir=parent_dir = "C:/Users/91931/Desktop/Scripting/python/os_module"
path=os.path.join(parent_dir,directory)
mode=0o666
os.mkdir(path,mode)
print("Directory '% s' created " % directory)
