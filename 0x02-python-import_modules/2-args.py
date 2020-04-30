#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count_arg = 0
    if len(argv) == 2:
        count_arg += 1
        print("{} argument:".format(count_arg))
        print("{} : {}".format(count_arg, argv[1]))
    elif len(argv) < 2:
        print("{} arguments.".format(count_arg))
    else:
        count_arg = len(argv) - 1
        print("{} arguments:".format(count_arg))
        for i in range(1, count_arg + 1):
            print("{} : {}".format(i, argv[i]))
