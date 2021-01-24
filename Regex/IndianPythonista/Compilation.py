import re
txt= """
The best thing about regex is that it makes the task of string manipulation so easy.
"""

pattern=re.compile("the", flags=re.I)
match=pattern.findall(txt)
print(match)


txt_1="""
A man was crossing the road.
Suddenly, a car passed before him in a very high speed.
He was terrified
And shocked.
"""

pattern=re.compile("^A.*", flags=re.M)
match=pattern.findall(txt_1)
print(match)
