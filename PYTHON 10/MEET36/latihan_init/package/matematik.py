def tambah(*data):
    hasil = 0
    for i in data:
        hasil += i
    return hasil

def kali(*data):
    hasil = 1
    for i in data:
        hasil *= i
    return hasil