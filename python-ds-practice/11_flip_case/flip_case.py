def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new = to_swap.lower()
    out = ""

    for letter in phrase:
        if letter.lower() == new:
            letter = letter.swapcase()
        out += letter

    return out

print(flip_case('Aaaahhh', 'h'))
