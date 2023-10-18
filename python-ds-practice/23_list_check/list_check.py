def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    lists = all(list in lst for list in lst)

    return lists

print(list_check([[1], [2, 3]]))