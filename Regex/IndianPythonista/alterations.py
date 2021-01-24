import re
##txt = """
##the most common conjunctions are and, or and but.
##"""
##pattern=re.compile("are|and|or")
##match=pattern.findall(txt)
##print(match)



txt= """
What is your name?
Who is that guy?
"""

#pattern=re.compile("What|Who is")
pattern = re.compile("What|Who is")
match=pattern.findall(txt)
print(match)
