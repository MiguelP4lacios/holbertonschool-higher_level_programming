#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nw = []
    for i in range(list_length):
        try:
            nw.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            nw.append(0)
            print("wrong type")
        except ZeroDivisionError:
            nw.append(0)
            print("division by 0")
        except IndexError:
            nw.append(0)
            print("out of range")
        finally:
            pass
    return nw
