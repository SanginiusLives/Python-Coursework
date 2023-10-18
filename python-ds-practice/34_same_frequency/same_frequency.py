def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return counter(str(num1)) == counter(str(num2))

def counter(coll):
    """Returns frequency counter mapping of coll."""

    count = {}

    for x in coll:
        count[x] = count.get(x, 0) + 1

    return count

print(same_frequency(551122, 221515))