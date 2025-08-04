''' This code lists all the files and directories in the root directory ("/").
    It uses the os.listdir function to get the list
    of files and directories in the specified path and then prints the results.  '''

import os
path="C:/Users/91931/Desktop/Scripting/python/os_module"

dir_list=os.listdir(path)
print("Files and directories in " , path," :")
print(dir_list)
