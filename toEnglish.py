from helpers.functions import functiontoenglish

def mapToEnglish(lom):

    sentence = []
    i = 0
    while(i<len(lom)):
        if lom[i]['Type'] == 'function':
            sentence.append(functiontoenglish(lom[i]['Value']))
        elif lom[i]['Type'] == 'ass':
            sentence.append(" is assigned to ")
        elif lom[i]['Type'] == 'float':
            sentence.append("the number " + lom[i]['Value'])
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
                if ((i>0) and (lom[i-1]['Type'] != 'float')):
                    sentence.append(" negative of ")
                else:
                    sentence.append(" subtracted by ")
            elif(lom[i]['Value'] == '*'):
                sentence.append(" multiplied with ")
            elif(lom[i]['Value'] == '/'):
                sentence.append(" divided by ")
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

    x =("".join(sentence))
    return(x[0].upper() + x[1:])

LOOPNAMES = {"for":" a for loop where ",
             "in":" in the ",
             "while": " a while loop where ",
             "if": " if ",
             "elif": " else "}

def loops(loopName):
    if loopName in LOOPNAMES:
        return LOOPNAMES[loopName]
    else:
        return -1

