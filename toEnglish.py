##test = [{'Value':'print','Type':'function'},{'Value':'7','Type':'float'},{'Value':'-','Type':'op'},{'Value':'6','Type':'float'}]
##
##test0 = [{'Value':'print','Type':'function'},{'Value':'abs','Type':'function'},{'Value':'8','Type':'float'}]
##
##test0 = {'Value':'x','Type':'var'},{'Value':'=','Type':'ass'},{'Value':'5','Type':'float'},{'Value':'+','Type':'op'},{'Value':'4','Type':'float'}
##
##test0 = {'Value':'for','Type':'loop'},{'Value':'i','Type':'var'},{'Value':'in','Type':'loop'},{'Value':[{'Value':'range','Type':'function'},{'Value':'0','Type':'float'},{'Value':',','Type':'op'},{'Value':'9','Type':'float'}],'Type':'forfunction'}
##
##test0 =  {'Value':'print','Type':'function'},{'Value':'abs','Type':'function'},{'Value':'-8','Type':'float'},{'Value':',','Type':'op'},{'Value':'9','Type':'float'}
##
##test1 = [{'Value':'print','Type':'function'},{'Value':'35','Type':'float'},{'Value':'.','Type':'decimal'},{'Value':'41','Type':'float'},{'Value':'+','Type':'op'},{'Value':'69','Type':'float'}]
##

def mapToEnglish(lom):

    sentence = []
    i = 0
    while(i<len(lom)):
        if lom[i]['Type'] == 'function':
            sentence.append(functiontoenglish(lom[i]['Value']))
        elif lom[i]['Type'] == 'ass':
            sentence.append(" is assigned to ")
        elif lom[i]['Type'] == 'float':
            if ((i<len(lom)-1) and ((lom[i+1]['Type'] == 'op'))) or ((i>0) and ((lom[i-1]['Type'] == 'op') or (lom[i-1]['Type'] == 'function'))):
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
            else:
                print("FUCK")

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

        else:
            print("SHIT")
        i = i + 1

    x =("".join(sentence))
    return(x[0].upper() + x[1:])



LOOPNAMES = {"for":"a for loop where ",
             "in":" in the "}

def loops(loopName):
    if loopName in LOOPNAMES:
        return LOOPNAMES[loopName]
    else:
        return -1

def main():

    print(mapToEnglish(test1))

main()

