import os

def new_directory(directory, filename):
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    os.chdir(directory)
    with open(filename,'w') as file:
        pass

    os.chdir('..')
    return os.listdir(directory)
    

print(new_directory("PythonPrograms","scripts.py"))