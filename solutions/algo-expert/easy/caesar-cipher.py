def caesarCipherEncryptor(string, key):
    # Write your code here.
    '''
    n = key
    shifting every char by n spaces

    shift means to incerase the char by n postions.
    a shift 3 means a->b->c->d, 3 arrows.

    ord(char) -> int
    chr(int) -> char
    96 -> a
    122->z
    '''

    res = []

    # key might loop over
    newKey = key % 26
    for khar in string:
        res.append(shift(khar, key))

    return "".join(res)


def shift(char, key):
    newCode = ord(char) + key
    return chr(newCode) if newCode <= 122 else chr(96 + newCode % 122)
