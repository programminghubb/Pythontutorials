import re

statement = "Learn python programming with us"

mobj = re.match( r'python', statement)
if mobj:
   print("Matched word : ", mobj.group())
else:
   print("No match found!")

sobj = re.search( r'python', statement)
if sobj:
   print("Searched word : ", sobj.group())
else:
   print("Nothing found!")
