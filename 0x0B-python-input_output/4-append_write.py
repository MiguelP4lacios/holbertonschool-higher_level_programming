#!/usr/bin/python3
"""Module that read a file and print your content
"""


def append_write(filename="", text=""):
        """Function that write a file whitout overwrite
        Args:
            filename (str, optional): path file. Defaults to "".
            text (str, optional): content. Defaults to "".
        """

        with open(filename, mode='a', encoding='utf-8') as afile:
                return (afile.write(text))
