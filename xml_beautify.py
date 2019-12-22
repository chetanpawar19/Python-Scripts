"""
Program to beautify unformatted xml file.
Note-provide xml file path
author-chetan pawar
"""

import re

file= open("test.xml", "r")
tab_count = 0

for line in file.readlines():
    if re.findall(r"<\?.*>",line)!=[]:            #to handle first <? xml ?> line
        print(tab_count*"   "+line, end="")
    elif re.findall(r"<.*>",line)!=[] and re.findall("</\w+>",line)==[] and re.findall(r"<\?.*>",line)==[]:
        print(tab_count*"   "+line,end="")
        tab_count = tab_count + 1
    elif re.findall("<\w+>",line)!=[] and re.findall("</\w+>",line)!=[]:
        print(tab_count*"   "+line,end="")
    elif re.findall("<\w+>",line)==[] and re.findall("</\w+>",line)!=[]:
        tab_count = tab_count - 1
        print(tab_count*"   "+line,end="")
    else:
        pass
