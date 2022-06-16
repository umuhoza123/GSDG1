
from unicodedata import name


list_animal=["Gorilla","hypotame","zebra","lion"]

for item in list_animal:
#    print(item + ' at ' + str(list_animal.index(item)))
    print(list_animal[1:3:2])
#  name='''
#    hhhhhhhhhhhhh
#    '''
#    print(name)


# input from user
name=input('enter name of animal')
list_animal.append(name)
print(list_animal)


