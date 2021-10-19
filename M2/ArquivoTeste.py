import os

def create_python_script(filename):
    comments = "#Start"
    with open(filename, 'w') as file:
        file = file.write(comments)
        filesize = os.path.getsize(file)

        return (filesize)

print(create_python_script("program.py"))


#corrigir