#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        man = "argument:"
    elif len(argv) < 2:
        man = "arguments."
    else:
        man = "arguments:"
    print("{} {}".format(len(argv) - 1, man))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
