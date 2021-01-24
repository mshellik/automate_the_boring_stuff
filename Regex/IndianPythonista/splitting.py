import re
txt = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

pattern=re.compile("\n")
match=pattern.split(txt)

##for text in match:
##    print(text)
##print(type(txt))

print(match)


pattern=re.compile("\W")
match=pattern.split(txt)
print(match)


match=pattern.split(txt, maxsplit=6)

print(match)
