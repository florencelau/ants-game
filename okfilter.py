

import sys

print ("""--------------------------------------------------
Usage: python3 ok -q 05 |python3 okfilter.py
 
Use Ctrl-D to break
--------------------------------------------------""")

f = open('unit.py', 'w')
failed = False
for line in sys.stdin:
    if line.startswith(">>>") | line.startswith('...'):
        f.write(line[4:])
        failed = True
        pass
    pass

pnow = True
def myprint(*args):
    if pnow:
        print (*args)
        pass
    pass

if failed : 
    myprint ("--------------------------------------------------")
    print ("""Unit test generated in 'unit.py'
    cat unit.py : to see the content
    python3 unit.py : to reproduce the test""")
    print ("--------------------------------------------------")
else :
    myprint ("--------------------------------------------------")
    print ("""PASS""")
    print ("--------------------------------------------------")

