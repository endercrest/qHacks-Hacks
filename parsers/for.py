import re
from helpers.functions import allfunctions
#  for
# i in range(0,9)
# i in "HI"

# for variable : {"value": "i", "type": "var"}
# for in : {"value" : "in", "type": "loop"} NOT SURE IF THIS IS THE TYPE WE WANT
# for range(0, 9): {"value": [{"value": "", "type": "function"}, {"value": 0, "type": "float"}, {"value": 9, type: "float"}], "type": "special"]

# f = [{"Value": "for", "Type": "loop"}, {"Value": "in", "Type": "loop"}]


def parsefor(raw):
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
        # TODO Call Sean's function to parse.
        lom.append({"Value": "TODO", "Type": "forfunction"})
    else:
        lom.append({"Value": combined, "Type": "forstring"})

    print(lom)

    return lom

parsefor("i in \"Hello!\"")
parsefor("i in range(0, 9)")