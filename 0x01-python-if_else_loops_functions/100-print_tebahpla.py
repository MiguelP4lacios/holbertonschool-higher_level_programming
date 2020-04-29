#!/usr/bin/python3
for i in range(-122, -96):
    if abs(i) % 2 == 1:
        i = abs(i) - 32
    print("{}".format(chr(abs(i))), end="")
