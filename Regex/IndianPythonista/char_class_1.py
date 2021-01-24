import re

txt="""
Yesterday, I was driving my car without a driving licence. The traffic police stopped me and asked me for my 
license. I told them that I forgot my licence at home. 
"""

pattern=re.compile("licen[cs]e")
match=pattern.findall(txt)
print(match)
