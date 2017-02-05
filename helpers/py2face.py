from Translate import parsefunction
from toEnglish import mapToEnglish

def pythontoenglish(input):
    return mapToEnglish(parsefunction(input))

#print(pythontoenglish("print(\"Hello World\")"))
#print(pythontoenglish("for i in range(0,9)"))