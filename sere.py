import re

address = "Wall street 19, New York"

add = re.sub(r'\d', "", address)
print("Address without digit: ", add)
