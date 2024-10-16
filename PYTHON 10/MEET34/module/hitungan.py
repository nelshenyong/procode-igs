def tambah(*data):
    h = 0
    for x in data:
        h += x
    return h

def pangkat(x):
    return lambda y : y ** x