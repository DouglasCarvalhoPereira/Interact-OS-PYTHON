import re

def refazendo_nomes(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result == None:
        return name

    return "{} {}".format(result[1], result[2])