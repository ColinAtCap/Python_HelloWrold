# Python loop program

animals = ['man','bear','pig','cow','duck','horse']
moreanimals = ['Whale','Lion']
moreanimals = sorted(moreanimals)

allanimals = animals+moreanimals

def listanimals(listname):
    index = 0
    print('\n')
    while index < len(listname):
        print(listname[index])
        index +=1

listanimals(allanimals)

allanimals.sort() # sort actual list

listanimals(allanimals)

