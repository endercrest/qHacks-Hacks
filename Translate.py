import re
from csv import reader

def split(string):
    for i in string:
        if i == ' ':
            linespl = (re.split(r'[ ]+', string))
            break
        elif i == '(':
            linespl = re.split(r'[(]+', string)
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
        elif countQ == 0 and (i.isdigit() or i == '.'):
            temp.append(i)
            restList.append(temp)
            temp = []
            continue
        elif countQ == 0 and i == ')':
            temp.append(i)
            restList.append(temp)
            temp = []
            continue
        elif countQ == 0 and (i == '+' or i == '-' or i == '/' or i == '*'):
            temp.append(i)
            restList.append(temp)
            temp = []
            continue
        elif countQ == 0 and i == '=':
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

 #   print(restList)

    lis = []
    lis.append({'Value': function, 'Type': 'function'})
    temp = []
    num = ''
    for i in restList:
        funcFound = False
        part = ''.join(i)
        for func in FUNCTION_DEFS:
            if part.find(func) >= 0:
                funcFound = True
                continue
        if i == ' ' or i == '':
            continue
        elif i[0].isdigit():
            temp.append(i[0])
            continue
        if i[0] == '+' or i[0] == '-' or i[0] == '/' or i[0] == '*' or i[0] == ',':
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
            lis.append({'Value': part, 'Type': 'string'})
            
    print(lis)

def main():
    string = 'print("Hello 2,World", round(3.14), 1=3+4, "T", abs(12))'
    print(string)
    function, rest = split(string)
    restFormat(function, rest)

main()
    
