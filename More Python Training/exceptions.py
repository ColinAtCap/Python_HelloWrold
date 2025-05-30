# trying exceptions

animals = ['dog','banana','bear','horse','dolphin']

def AmIThere(find):
    try:
        cat_index = animals[animals.index(find)]
    except:
        cat_index = 'No '+find
    print('\n',cat_index)

AmIThere(find='dog')
