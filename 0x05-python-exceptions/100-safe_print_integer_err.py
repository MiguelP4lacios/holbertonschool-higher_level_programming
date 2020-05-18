#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    strmen = "Exception: "
    try:
        print("{:d}".format(value))
        return True
    except ValueError as men:
        strmen += str(men)
        strmen += "\n"
        sys.stderr.write(strmen)
        return False
    except TypeError:
        return False
