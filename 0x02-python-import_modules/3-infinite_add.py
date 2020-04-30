#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    suma = 0
    for i in argv[1:]:
        suma += int(i)
    print(suma)
