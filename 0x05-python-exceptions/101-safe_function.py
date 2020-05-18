#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    strmen = "Exception: "
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError) as men:
        strmen += str(men)
        strmen += "\n"
        sys.stderr.write(strmen)
        return None
