# tuple python

animals = ['dog','banana','bear','horse','dolphin']
print('\n')
for x in animals:
    print(x.upper())

tanimals = tuple(animals)
print('\n')
for x in tanimals:
    print(x.upper())
# tuple python
print('animals list is {}.'.format(type(animals)))
print('tanimals list is {}.'.format(type(tanimals)))

for animal in tanimals:
    print(animal.upper())