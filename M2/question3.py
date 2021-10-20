import os
import datetime

def file_date(filename):
    os.getcwd()
    with open(filename,'w') as file:
        horario = os.path.getmtime(filename)

    timestamp = datetime.datetime.fromtimestamp(horario)

    return ("{:%Y-%m-%d}".format(timestamp))

print(file_date("newfile.txt"))