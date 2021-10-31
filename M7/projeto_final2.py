#!/usr/bin/env python
import re
import operator

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
resultInfo = re.search(r"ticky: INFO: ([\w ]*) ", line)
#regexName = r"\([\w+ \.]*\)$"
regexName = r"\((\w+)\)$"
result = re.search(regexName, line)
username = re.search(r"\(\b[\w+ \.]*\b\)$", line)
print(resultInfo)
print(result[1])

#line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Created ticket [#1234] (username)"
#resultError = re.search(r"ticky: ERROR: ([\w ]*) ", line)
#print(resultError)

#fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
#print(sorted(fruit.items())) # Organizando pelas chaves
#print(sorted(fruit.items(), key=operator.itemgetter(1))) # Organizando pelos valores
#print(sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)) # Inverte a Ordem