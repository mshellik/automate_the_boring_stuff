import re
pattern=re.compile("My Name is Mahesh Shellikeri and I am from Gadag")
match=pattern.match("My")
print(match)
