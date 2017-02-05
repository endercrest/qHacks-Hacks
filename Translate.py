import re
from helpers.functions import allfunctions

FUNCTION_DEFS = {
    'abs(', 'dict(', 'help(', 'min(', 'setattr(', 'all(', 'dir(', 'hex(', 'next(', 'slice(',
    'any(', 'divmod(', 'id(', 'object(', 'sorted(', 'ascii(', 'enumerate(', 'input(', 'oct(',
    'staticmethod(', 'bin(', 'eval(', 'int(', 'open(', 'str(', 'bool(', 'exec(', 'isinstance(',
    'ord(', 'sum(', 'bytearray(', 'filter(', 'issubclass(', 'pow(', 'super(', 'bytes(', 'float(',
    'iter(', 'print(', 'tuple(', 'callable(', 'format(', 'len(', 'property(', 'type(', 'chr(',
    'frozenset(', 'list(', 'range(', 'vars(', 'classmethod(', 'getattr(', 'locals(', 'repr(', 'zip(',
    'compile(', 'globals(', 'map(', 'reversed(', 'complex(', 'hasattr(', 'max(', 'round(', 'delattr(',
    'hash(', 'memoryview(', 'set('
}

SPECIAL_CHARS = {
    '+': 'op', '-': 'op', '/': 'op', '*': 'op', ',': 'op', '<': 'op', '>': 'op', '.': 'decimal', ')': 'bracket',
    '=': 'ass'
}


def split(string):
    for i in string:
        if i == ' ':
            linespl = (re.split(r'[ ]+', string, 1))
            break
        elif i == '(':
            linespl = re.split(r'[(]+', string, 1)
            break
    return linespl[0], linespl[1]


def parseExpression(rest):
    restList = []
    temp = []
    countQ = 0
    digitFlag = 0
    prev = ''
    for i in rest:
        if i == '"':
            countQ += 1
            if countQ == 2:
                countQ = 0
                temp.append('"')
                restList.append(temp)
                temp = []
                prev = '"'
                continue
        if countQ == 1:
            if i == '"':
                temp.append('"')
                prev = '"'
            else:
                temp.append(i)
                prev = i
            continue
        if countQ == 0 and i == ',':
            temp.append(',')
            restList.append(temp)
            temp = []
            prev = ','
            continue
        elif countQ == 0 and (i.isdigit() or i == '.'):
            temp.append(i)
            restList.append(temp)
            temp = []
            prev = i
            continue
        elif countQ == 0 and ((i == '+' or i == '-' or i == '/' or i == '*') or i == ')' or (i == '<' or i == '>') or i == '='):
            if temp is not [] and prev is not '=':
                restList.append(temp)
                temp = []
            if i == '=' and prev == '=':
                temp.append('==')
                restList[-1] = temp
                prev = '=='
            else:
                temp.append(i)
                restList.append(temp)
                prev = i
            temp = []
            continue
        elif i is not ' ':
            temp.append(i)
            prev = i
            if i == '(':
                restList.append(temp)
                temp = []
                continue

    # print(restList)

    lis = []
    temp = []
    num = ''
    for i in restList:
        print(i)
        funcFound = False
        part = ''.join(i)
        if part in FUNCTION_DEFS:
            funcFound = True
        if i == ' ' or i == '' or i == []:
            continue
        elif i[0].isdigit():
            temp.append(i[0])
            continue
        if i[0] == '+' or i[0] == '-' or i[0] == '/' or i[0] == '*' or i[0] == '<' or i[0] == '>' or i[0] == ',':
            num = ''.join(temp)
            if num is not '':
                lis.append({'Value': num, 'Type': 'float'})
            lis.append({'Value': part, 'Type': 'op'})
            num = ''
            temp = []
        elif i[0] == '.':
            num = ''.join(temp)
            if num is not '':
                lis.append({'Value': num, 'Type': 'float'})
            lis.append({'Value': part, 'Type': 'decimal'})
            num = ''
            temp = []
        elif i[0] == '=':
            num = ''.join(temp)
            if num is not '':
                lis.append({'Value': num, 'Type': 'float'})
            lis.append({'Value': part, 'Type': 'ass'})
            num = ''
            temp = []
        elif i[0] == '==':
            num = ''.join(temp)
            if num is not '':
                lis.append({'Value': num, 'Type': 'float'})
            lis.append({'Value': part, 'Type': 'cmp'})
            num = ''
            temp = []
        elif i[0] == ')':
            num = ''.join(temp)
            if num is not '':
                lis.append({'Value': num, 'Type': 'float'})
            lis.append({'Value': part, 'Type': 'bracket'})
            num = ''
            temp = []
        elif funcFound == True:
            lis.append({'Value': part, 'Type': 'function'})
            funcFound = False
        else:
            if part[0] is not '"':
                last = part[-1]
                start = part[:-1]
                if last not in SPECIAL_CHARS:
                    lis.append({'Value': part, 'Type': 'var'})
                else:
                    lis.append({'Value': start, 'Type': 'var'})
                    lis.append({'Value': last, 'Type': SPECIAL_CHARS[last]})
            else:
                lis.append({'Value': part, 'Type': 'string'})
    print(lis)
    return lis


def parseif(raw):
    """
    Parses a string in the format of a while statement.

    :param raw: The raw form of the for loop. IE. "i in range(0,9)"
    :return: Returns a list of maps.
    """
    lom = [{"Value": "if", "Type": "conditional"}]

    return lom


def parsefor(raw):
    """
    Parses a string in the format of a for statement.

    :param raw: The raw form of the for loop. IE. "i in range(0,9)"
    :return: Returns a list of maps.
    """
    lom = [{"Value": "for", "Type": "loop"}]

    parts = []
    for i in raw:
        if i == ' ':
            parts = (re.split(r'[ ]+', raw))

    lom.append({"Value": parts[0], "Type": "var"})
    lom.append({"Value": parts[1], "Type": "loop"})
    # Determine if function
    combined = ""
    for i in range(2, len(parts)):
        combined += " " + parts[i]
    if parts[2].split("(")[0] in allfunctions():
        lom.append({"Value": parsefunction(combined), "Type": "forfunction"})
    else:
        lom.append({"Value": combined, "Type": "forstring"})

    return lom


def whileparse(raw):
    """
    Parses a string in the format of a while statement.

    :param raw: The raw form of the for loop. IE. "i in range(0,9)"
    :return: Returns a list of maps.
    """
    lom = [{"Value": "while", "Type": "loop"}]

    bracket = False
    for i in raw:
        if i == "(":
            bracket = True
            break
        elif i == " ":
            raw = raw[1:]
        else:
            break
    if raw[-1:] == ":":
        raw = raw[:-1]
    expression = raw
    if bracket:
        expression = raw[1:-1]

    parseExpression(expression)

    lom.append({"Value": parseExpression(expression), "Type": "loop"})

    return lom


def parsefunction(string):
    function, rest = split(string)

    if function == "while":
        return whileparse(rest)
    elif function == "if":
        return parseif(rest)
    elif function == "for":
        return parsefor(rest)

    ls = (parseExpression(rest))
    if function is not 'for' or function is not 'while' or function is not 'if':
        ls.insert(0, {'Value': function+'(', 'Type': 'function'})
    return ls

print(parsefunction("print(1 + 12 + 3)"))
