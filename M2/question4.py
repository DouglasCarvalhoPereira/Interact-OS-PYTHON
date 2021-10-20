import os

def parent_directory():
    relative_parent = os.path.dirname(os.getcwd())
    os.chdir(relative_parent)
    return(os.getcwd())

print(parent_directory())