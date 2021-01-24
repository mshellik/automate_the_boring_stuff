import re

txt = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

##pattern=re.compile("[1-9][0-9][0-9][0-9]")
##match=pattern.findall(txt)
##print(match)
##
##pattern=re.compile("[^aeiou]")
##match=pattern.findall(txt)
##print(match)
##
##pattern=re.compile("[0-9]\d\d\d")
##match=pattern.findall(txt)
##print(match)

##pattern=re.compile("[^\w\s]")
##match=pattern.findall(txt)
##print(match)


pattern=re.compile("[^aeiou\n\(\)]")
match=pattern.findall(txt)
print(match)
