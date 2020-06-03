#!/usr/bin/python3
"""Module that read a file and print your content
"""


def write_file(filename="", text=""):
        """Function that write a file
        Args:
            filename (str, optional): path file. Defaults to "".
            text (str, optional): content. Defaults to "".
        """

        with open(filename, mode='w', encoding='utf-8') as afile:
                return (afile.write(text))
