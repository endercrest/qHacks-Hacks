test2 =[{'Value':'x','Type':'var'},{'Value':'=','Type':'ass'},{'Value':'5','Type':'int'},{'Value':'+','Type':'op'},{'Value':'4','Type':'int'}]

test1 = [{'Value':'print','Type':'function'},{'Value':'7.0','Type':'float'},{'Value':'+','Type':'op'}]

test4 = [{'Value':'/','Type':'op'}]

test0 = {'Value':'x','Type':'var'},{'Value':'=','Type':'ass'},{'Value':'5','Type':'int'},{'Value':'+','Type':'op'},{'Value':'4','Type':'int'}

def main():

    sentence = []
    for i in range (0,len(test1)):
        if test1[i]['Type'] == 'function':
            sentence.append(functiontoenglish(test1[i]['Value']))
        elif test1[i]['Type'] == 'ass':
            sentence.append(" is assigned to ")
        elif test1[i]['Type'] == 'int':
            sentence.append("the integer " + test1[i]['Value'])
        elif test1[i]['Type'] == 'string':
            if ((i<len(test1)-1) and (test1[i+1]['Type'] == 'op')) or ((i<0) and (test1[i-1]['Type'] == 'op')):
                sentence.append("the integer " + test1[i]['Value'])
            else:
                sentence.append("the string " + test1[i]['Value'])
        elif test1[i]['Type'] == 'var':
            sentence.append("the variable " + test1[i]['Value'])
        elif test1[i]['Type'] == 'comma':
            sentence.append(" and then it")
        elif test1[i]['Type'] == 'op':
            if(test1[i]['Value'] == '+'):
                sentence.append(" added with ")
            elif(test1[i]['Value'] == '-'):
                sentence.append(" subtracted by ")
            elif(test1[i]['Value'] == '*'):
                sentence.append(" multiplied with ")
            else:
                sentence.append(" divided by ")
        else:
            print("else clause")

    print("".join(sentence))


FUNCTION_DEFS = {
    "abs": "Absolute value of {}.",
    "all": "The boolean if all of these elements are true: ",
    "any": "The boolean if any of these elements are true: ",
    # "basestring": "",
    "bin": "The binary string of ",
    "bool": "The boolean value of ",
    # "bytearray": "",
    # "callable": "",
    "chr": "The character string of ",
    # "classmethod": "",
    "cmp": "Compares ",
    # "compile": "",
    # "complex": "",
    # "delattr": "",
    # "dict": "",
    # "dir": "",
    "divmod": "The quotient and remainder of ",
    # "enumerate": "",
    "eval": "The evaluated expression of ",
    # "execfile": "",
    # "file": "",
    # "filter": "",
    "float": "The floating point of ",
    # "format": "",
    # "frozenset": "",
    # "getattr": "",
    # "globals": "",
    # "hasattr": "",
    "hash": "The hash value of {}",
    "help": "Starts the interactive help interpreter. ",
    "hex": "The hexadecimal number of ",
    "id": "The unique id of {}",
    "input": "Prompts for input of ",
    "int": "The integer of ",
    # "isinstance": "",
    # "issubclass": "",
    # "iter": "",
    "len": "The length of ",
    "list": "The list of ",
    # "locals": "",
    "long": "The long of ",
    # "map": "",
    "max": "The maximum value of ",
    "memoryview": "Memory view of ",
    "min": "The minimum value of ",
    "next": "The next value of ",
    # "object": "",
    "oct": "The octal string of ",
    # "open": "",
    "ord": "The unicode of ",
    "pow": "The power of ",
    "print": "Prints ",
    # "property": "",
    "range": "Range of {}",
    "raw_input": "Prompts for raw input of ",
    # "reduce": "",
    "reload": "Reloads {}",
    "repr": "Printable version of ",
    "reversed": "The reverse of ",
    "round": "Rounds {}",
    "set": "A new set of ",
    # "setattr": "",
    # "slice": "",
    "sorted": "The sorted of ",
    # "staticmethod": "",
    "str": "Printable version of ",
    "sum": "The sum of ",
    # "super": "",
    # "tuple": "",
    "type": "The type of ",
    "unichr": "The unicode of ",
    # "vars": "",
    "xrange": "The range of ",
    # "zip": "",
    "__import__": "Imports "
}

def functiontoenglish(name):
    """"
    Converts the given function to english version of what it does. The string will
    contain a {} of where the rest of the text should go.

    If the function is not found, the function will return -1.
    """
    if name in FUNCTION_DEFS:
        return FUNCTION_DEFS[name]
    else:
        return -1


main()


