cats={'Name':'Bekku','Color':'Grey','Age': '8'}
pussy={'Age':'8','Name':'Bekku', 'Color': 'Grey'}
##print(cats)
##print(pussy)
##print('Compare Dicts eventhough the keys/value are not in the same order')
##print('cats==pussy  ',cats==pussy)
##print('cats!=pussy  ', cats!=pussy)
##
##
##print('The Values of the keys and will be printed in LIST')
##print("cats['Name'] =", cats['Name'])
##print(list((cats.values())))
##
##print('The Keys of the Dicts' )
##print(pussy.keys())
##print(list((pussy.values())))
##
##
##print('Loop Through the keys of the Dict')
##for k in cats.keys():
##    print(k)
##
##print('Loop Through the values of the Dict')
##for v in pussy.values():
##    print(v)
##
##print('Loop through each pair of key/value and will print as tupple')
##for items in cats.items():
##    print(items)


print('Checking if the value exists in a Dict or not')

print('Bekku' in cats.values())

print('Kunni' not in cats.values())

print('Kaami' in cats.values())
