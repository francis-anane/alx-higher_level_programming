#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ This function divides element by element 2 lists.
    """

    result = 0
    i = 0
    new_list = []
    while list_length > 0:
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            list_length -= 1
            i += 1
    return new_list
