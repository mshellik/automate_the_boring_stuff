import re
txt = """<html><head><title>Title</title>"""

pattern=re.compile("<.*>")
match=pattern.findall(txt)
print(match)

pattern=re.compile("<.*?>")
match=pattern.findall(txt)
print(match)


txt_1="""
555-555-5555
555 555 5555
5555555555
"""

pattern_1=e.compile("\d{3}[-\s]?-\d{3}[-\s]?\d{4}")
match=pattern_1.findall(txt_1)
