import re
from helpers.functions import functiontoenglish


def mapToEnglish(lom):

    sentence = []
    i = 0
    while(i<len(lom)):
        print(lom[i]['Type'],(i,lom[i]['Value'], len(lom)))
        if lom[i]['Type'] == 'function':
            sentence.append(functiontoenglish(lom[i]['Value']))
        elif lom[i]['Type'] == 'ass':
            sentence.append(" is assigned to ")
        elif lom[i]['Type'] == 'float':
            if ((i<len(lom)-1) and ((lom[i+1]['Type'] == 'op'))) or ((i>0) and ((lom[i-1]['Type'] == 'op') or (lom[i-1]['Type'] == 'function' or (lom[i-1]['Type'] == 'cmp')))):
                sentence.append("the number " + lom[i]['Value'])
            else:
                sentence.append("the string " + lom[i]['Value'])
        elif lom[i]['Type'] == 'string':
                sentence.append("the string " + lom[i]['Value'])
        elif lom[i]['Type'] == 'var':
            sentence.append("the variable " + lom[i]['Value'])
        elif lom[i]['Type'] == 'comma':
            sentence.append(" and then it")
        elif lom[i]['Type'] == 'op':
            if(lom[i]['Value'] == '+'):
                sentence.append(" added with ")
            elif(lom[i]['Value'] == '-'):
                sentence.append(" subtracted by ")
            elif(lom[i]['Value'] == '*'):
                sentence.append(" multiplied with ")
            elif(lom[i]['Value'] == '/'):
                sentence.append(" divided by ")
            elif(lom[i]['Value'] == '.'):
                sentence.append(" DECIMAL ")
            elif(lom[i]['Value'] == ','):
                sentence.append(" and ")
            elif(lom[i]['Value'] == '>'):
                sentence.append(" is checked to see if it's greater than ")
            elif(lom[i]['Value'] == '<'):
                sentence.append(" is checked to see if it's less than ")
            else:
                print("FUCK")

        elif(lom[i]['Type'] == 'cmp'):
            sentence.append(" compared to ")
                
        elif(lom[i]['Type'] == 'forfunction'):
            print (i, lom[i]['Type'], lom[i]['Value'])
            sentence.append(mapToEnglish(lom[i]['Value']))

        elif(lom[i]['Type'] == 'forstring'):
            sentence.append(lom[i]['Value'])

        elif(lom[i]['Type'] == 'loop'):
            sentence.append(loops(lom[i]['Value']))

        elif(lom[i]['Type'] == 'decimal'):
            if(lom[i-1]['Type'] == "float"):
                sentence.append(lom[i-1]['Value'].strip('.0') + "." + lom[i+1]['Value'].strip('.0'))
                sentence[i-1] = ''
            i = i + 1
        i = i + 1

    print(sentence)
    x =("".join(sentence))
    return(x[0].upper() + x[1:])

LOOPNAMES = {"for":" a for loop where ",
             "in":" in the "}

def loops(loopName):
    if loopName in LOOPNAMES:
        return LOOPNAMES[loopName]
    else:
        return -1


##################################################################################################################################################


FUNCTION_DEFS = {
    'abs(', 'dict(', 'help(', 'min(', 'setattr(', 'all(', 'dir(', 'hex(', 'next(', 'slice(',
    'any(', 'divmod(', 'id(', 'object(', 'sorted(', 'ascii(', 'enumerate(', 'input(', 'oct(',
    'staticmethod(', 'bin(', 'eval(', 'int(', 'open(', 'str(', 'bool(', 'exec(', 'isinstance(',
    'ord(', 'sum(', 'bytearray(', 'filter(', 'issubclass(', 'pow(', 'super(', 'bytes(', 'float(',
    'iter(', 'print(', 'tuple(', 'callable(', 'format(', 'len(','property(', 'type(', 'chr(',
    'frozenset(', 'list(', 'range(', 'vars(','classmethod(', 'getattr(', 'locals(', 'repr(', 'zip(',
    'compile(', 'globals(', 'map(', 'reversed(', 'complex(', 'hasattr(', 'max(', 'round(', 'delattr(',
    'hash(', 'memoryview(', 'set('
}

SPECIAL_CHARS = {
    '+':'op', '-':'op', '/':'op', '*':'op', ',':'op', '<':'op', '>':'op', '.':'decimal', ')':'bracket', '=':'ass'
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

def restFormat(function, rest):
    restList = []
    temp = []
    countQ = 0
    digitFlag = 0
    for i in rest:
        if i == '"':
            countQ += 1
            if countQ == 2:
                countQ = 0
                temp.append('"')
                restList.append(temp)
                temp = []
                continue
        if countQ == 1:
            if i == '"':
                temp.append('"')
            else:
                temp.append(i)
            continue
        if countQ == 0 and i == ',':
            temp.append(',')
            restList.append(temp)
            temp = []
            continue
        elif countQ == 0 and ((i.isdigit() or i == '.') or (i == '+' or i == '-' or i == '/' or i == '*') or  i == ')' or i == '=' or (i == '<') or (i == '>')):
            if restList[-1][-1] == '=' and i == '=':
                temp.append('==')
                restList[-1] = temp
            else:
                temp.append(i)
                restList.append(temp)
            temp = []
            continue
        elif i is not ' ':
            temp.append(i)
            if i == '(':
                restList.append(temp)
                temp = []
                continue

    lis = []
    if function.find('for') == False:
        lis.append({'Value': function+'(', 'Type': 'function'})
    else:
        lis.append({'Value': function, 'Type': 'function'})
    temp = []
    num = ''
    for i in restList:
        funcFound = False
        part = ''.join(i)
        if part in FUNCTION_DEFS:
            funcFound = True
        if i == ' ' or i == '':
            continue
        elif i[0].isdigit():
            temp.append(i[0])
            continue
        if i[0] == '+' or i[0] == '-' or i[0] == '/' or i[0] == '*' or i[0] == ',' or i[0] == '<' or i[0] == '>':
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
    return lis            

def main():
    string = 'for i in range(0,9))'
    print(string)
    function, rest = split(string)
    lis = restFormat(function, rest)
    print(mapToEnglish(lis))

main()
