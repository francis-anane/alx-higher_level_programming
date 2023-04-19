#!/usr/bin/python3

""" 5-text_indentation module for printing two new lines after a character.
"""


def text_indentation(text):
    """Prints 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): the text data to print
    Raises:
          TypeError: If text is not a string.
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        new_text = ""
        for c in text:
            new_text += c
            if c in [".", "?", ":"]:
                new_text += "\n\n"

        data = list(new_text.split("\n"))
        data_len = len(data)
        chk_print = 0
        for line in data:
            if not line.startswith(" "):
                if chk_print != data_len - 1:
                    print(line)
                else:
                    print(line, end="")
            else:
                if chk_print != data_len - 1:
                    print(line.strip(" "))
                else:
                    print(line.strip(" "), end="")
            chk_print += 1
