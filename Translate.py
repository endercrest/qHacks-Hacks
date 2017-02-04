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
    
   # print(linespl)
    
 #   line = re.split(r'[(]+', string)
#    print(line)

def restFormat(function, rest):
 #   r = re.compile(r'(?:[^,(]|\([^)]*\))+')
 #   r.findall(rest)

    restList = []
    
    for line in reader(rest):
        if line[0] == '1':
            print(True)
        restList.append(line)
    
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
            
    print(lis)
 #   other = (re.split(r'[,)]+', rest))
 #   formatString = 
#    codeDict = {'Value': other[0], 'Type': 
#    print (insideQ)
   # print(insideQ)

def main():
    function, rest = split('print("Hello 2,World", "1", "Test")')
    restFormat(function, rest)

main()



    
