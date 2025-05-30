# dictionary python pogram

dict = {'a': [999,5,54], 'b': 2, 'c': 3, 'd': 4, 'end': 5}
dict['f'] = 6
del dict['end']  # Remove key 'b'
# Python program to demonstrate dictionary usage
print(dict)
print(len(dict))
def print_dictionary():
    for key, value in dict.items():
        print('\n')
        col=len(f"{value}")  # Get the length of the value     
        print('Length',col)
        if col == 1:
            print("The dictionary value for ")
            print(key)  
            print('is ') 
            print(f"{key}: {value}")                 
        else:
            print("The dictionary value for ")
            print(key)  
            print('is ') 
            print(f"{key}: {value[0]}")   

print_dictionary()

print(2 in dict.values())  # Check if 'a' is in the values
