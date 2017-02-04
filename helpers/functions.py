FUNCTION_DEFS = {
    "abs": "Absolute value of {}.",
    "all": "The boolean if all elements({}) are true.",
    "any": "The boolean if any elements({}) are true.",
    # "basestring": "",
    "bin": "The binary string of {}.",
    "bool": "The boolean value of {}.",
    # "bytearray": "",
    # "callable": "",
    "chr": "The character string of {}.",
    # "classmethod": "",
    "cmp": "Compares {}.",
    # "compile": "",
    # "complex": "",
    # "delattr": "",
    # "dict": "",
    # "dir": "",
    "divmod": "The quotient and remainder of {}.",
    # "enumerate": "",
    "eval": "The evaluated expression of {}",
    # "execfile": "",
    # "file": "",
    # "filter": "",
    "float": "The floating point of {}",
    # "format": "",
    # "frozenset": "",
    # "getattr": "",
    # "globals": "",
    # "hasattr": "",
    "hash": "The hash value of {}",
    "help": "Starts the interactive help interpreter. {}",
    "hex": "The hexadecimal number of {}",
    "id": "The unique id of {}",
    "input": "Prompts for input of {}",
    "int": "The integer of {}",
    # "isinstance": "",
    # "issubclass": "",
    # "iter": "",
    "len": "The length of {}",
    "list": "The list of {}",
    # "locals": "",
    "long": "The long of {}",
    # "map": "",
    "max": "The maximum value of {}",
    "memoryview": "Memory view of {}",
    "min": "The minimum value of {}",
    "next": "The next value of {}",
    # "object": "",
    "oct": "The octal string of {}",
    # "open": "",
    "ord": "The unicode of {}",
    "pow": "The power of {}",
    "print": "Prints {}",
    # "property": "",
    "range": "Range of {}",
    "raw_input": "Prompts for raw input of {}",
    # "reduce": "",
    "reload": "Reloads {}",
    "repr": "Printable version of {}",
    "reversed": "The reverse of {}",
    "round": "Rounds {}",
    "set": "A new set of {}",
    # "setattr": "",
    # "slice": "",
    "sorted": "The sorted of {}",
    # "staticmethod": "",
    "str": "Printable version of {}",
    "sum": "The sum of {}",
    # "super": "",
    # "tuple": "",
    "type": "The type of {}",
    "unichr": "The unicode of {}",
    # "vars": "",
    "xrange": "The range of {}",
    # "zip": "",
    "__import__": "Imports {}"
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