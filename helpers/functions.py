FUNCTION_DEFS = {
    "abs": "absolute value of ",
    "all": "the boolean if all of these elements are true: ",
    "any": "the boolean if any of these elements are true:",
    # "basestring": "",
    "bin": "the binary string of ",
    "bool": "the boolean value of ",
    # "bytearray": "",
    # "callable": "",
    "chr": "the character string of ",
    # "classmethod": "",
    "cmp": "compares ",
    # "compile": "",
    # "complex": "",
    # "delattr": "",
    # "dict": "",
    # "dir": "",
    "divmod": "the quotient and remainder of ",
    # "enumerate": "",
    "eval": "the evaluated expression of ",
    # "execfile": "",
    # "file": "",
    # "filter": "",
    "float": "the floating point of ",
    # "format": "",
    # "frozenset": "",
    # "getattr": "",
    # "globals": "",
    # "hasattr": "",
    "hash": "the hash value of ",
    "help": "starts the interactive help interpreter. ",
    "hex": "the hexadecimal number of ",
    "id": "the unique id of ",
    "input": "prompts for input of ",
    "int": "The integer of ",
    # "isinstance": "",
    # "issubclass": "",
    # "iter": "",
    "len": "the length of ",
    "list": "the list of ",
    # "locals": "",
    "long": "the long of ",
    # "map": "",
    "max": "the maximum value of ",
    "memoryview": "memory view of ",
    "min": "the minimum value of ",
    "next": "the next value of ",
    # "object": "",
    "oct": "the octal string of ",
    # "open": "",
    "ord": "the unicode of ",
    "pow": "the power of ",
    "print": "prints ",
    # "property": "",
    "range": "range of ",
    "raw_input": "prompts for raw input of ",
    # "reduce": "",
    "reload": "reloads ",
    "repr": "printable version of ",
    "reversed": "the reverse of ",
    "round": "rounds ",
    "set": "a new set of ",
    # "setattr": "",
    # "slice": "",
    "sorted": "the sorted of ",
    # "staticmethod": "",
    "str": "printable version of ",
    "sum": "the sum of ",
    # "super": "",
    # "tuple": "",
    "type": "the type of ",
    "unichr": "the unicode of ",
    # "vars": "",
    "xrange": "the range of ",
    # "zip": "",
    "__import__": "imports "
}


def functiontoenglish(name):
    """
    Converts the given function to english version of what it does. The string will
    contain a {} of where the rest of the text should go.

    :return: If the function is not found, the function will return -1.
    """
    if name in FUNCTION_DEFS:
        return FUNCTION_DEFS[name]
    else:
        return -1


def allfunctions():
    """
    This function returns a list of all the functions that have an english translation.
    :return: A list of function names.
    """
    return FUNCTION_DEFS.keys()
