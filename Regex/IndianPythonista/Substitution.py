import re
txt="100 cats, 23 dogs, 3 rabbits"

##pattern=re.compile("\d+")
##match=pattern.sub("-", txt)
##print(match)
##
##
##match=pattern.subn("-",txt)
##print(match)

pattern=re.compile("\d+")
match=pattern.subn("#",txt)[1]
print(match)
