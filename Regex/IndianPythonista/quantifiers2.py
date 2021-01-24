import re

txt = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

pattern=re.compile("[0-9]\d{3}")
match=pattern.findall(txt)
print(match)


txt_1 = """
123143
432
5657
4435
54
65111
"""

pattern=re.compile("\d{4,}")
match=pattern.findall(txt_1)
print(match)
