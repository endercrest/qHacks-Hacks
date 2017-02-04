import re
from csv import reader

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

def split(string):
    for i in string:
        if i == ' ':
            linespl = (re.split(r'[ ]+', string, 1))
            break
        elif i == '(':
            linespl = re.split(r'[(]+', string, 1)
            break

    return linespl[0], linespl[1]
    
   # print(linespl)
    
 #   line = re.split(r'[(]+', string)
#    print(line)

def restFormat(function, rest):
 #   r = re.compile(r'(?:[^,(]|\([^)]*\))+')
 #   r.findall(rest)

##    findF = ''
##    listOfFs = []
##    countQs = 0
##    for el in rest:
##        if el[0] == '"' and (countQs is not 2):
##            countQs += 1
##            continue
##        else:
##            findF += el
##        if countQs == 2:
##            countQs = 0
##            print(findF)
##            findF = ''

    listOfFs = []
    for func in FUNCTION_DEFS:
        index = rest.find(func)
        if index >= 0:
            listOfFs.append({'Func': func, 'Index': index}) 
            print(func, index)

    restList = []
    for line in reader(rest):
        if line == 
        restList.append(line)
    print(restList)

    lis = []
    lis.append({'Value': function, 'Type': 'function'})

    for i in restList:
        if i[0] == ' ' or i[0] == '' or i[0] == ')':
            continue
        if i[0].isdigit():
            i = float(i[0])
        if type(i) is float:
            lis.append({'Value': i, 'Type': 'float'})
        elif i[0] == '+' or i[0] == '-' or i[0] == '/' or i[0] == '*':
           lis.append({'Value': i[0], 'Type': 'op'})
        elif i[0] == '=':
            lis.append({'Value': i[0], 'Type': 'ass'})
        elif type(i[0]) is str:
            lis.append({'Value': i[0], 'Type': 'string'})
        else:
            lis.append({'Value': i[0], 'Type': 'function'})
            
 #   print(lis)
 #   other = (re.split(r'[,)]+', rest))
 #   formatString = 
#    codeDict = {'Value': other[0], 'Type': 
#    print (insideQ)
   # print(insideQ)

def main():
    function, rest = split('print("Hello 2,World", round(3.14), "1", "T", abs(12))')
    print(function)
    print(rest)
    restFormat(function, rest)

main()



##    restList = []
##    fullFunc = []
##    count = 0
##    funcCount = 0
##    for line in reader(rest):
##        print(len(line))
##        if count >= int(listOfFs[funcCount]['Index']):
##            fullFunc.append(line)
##            count += 1
##            continue
##        elif count == len(listOfFs[funcCount]['Func'])+count:
##            restList.append(fullFunc)
##            count += 1
##            funcCount = 0
##            continue
##        restList.append(line)
##        count += 1
##    print(restList)



    
