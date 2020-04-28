#!/usr/bin/python3
def uppercase(str):
    for i in str:
        lyrics = ord(i)
        if i.islower():
            lyrics -= 32
        print("{}".format(chr(lyrics)), end="")
    print()
