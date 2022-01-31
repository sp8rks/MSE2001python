def name_joiner(first_name, last_name):
    full_name = first_name + " " + last_name
    print(full_name)
    return first_name, last_name, full_name


the_first_name, the_last_name, the_full_name = name_joiner("taylor", "sparks")


def add_em_up(*items):
    summation = 0
    for catfish in items:
        summation = summation + catfish
    return summation


list_of_nums = [5, 6, 8, 10, 11]

total_sum = add_em_up(*list_of_nums)


name_dict = {"formula": "ABO3"}


def formula_printer(**kwargs):
    print(kwargs["formula"])


formula_printer(**name_dict)


# %%
def my_recursion(i):
    """
    prints value of integer and then reduces its by 1 each time
    only prints until i <1
    Parameters
    ----------
    i : int
        value to be printed and iterated.

    Returns
    -------
    None.

    """
    if i < 1:
        return None
    else:
        print(i)
    i = i - 1
    my_recursion(i)


my_recursion(5)
