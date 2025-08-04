''' The code checks and displays 
the current working directory (CWD) twice:
before and after changing the directory up one level
using os.chdir('../').
It provides a simple example of
how to work with the current working directory in Python.'''

import os
def current_path():
  print("Current working directory before")
  print(os.getcwd())
  print()

current_path()
os.chdir('../')
current_path()  