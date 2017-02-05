import re
from helpers.functions import allfunctions
from Translate import parse

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
        lom.append({"Value": parse(combined), "Type": "forfunction"})
    else:
        lom.append({"Value": combined, "Type": "forstring"})

    return lom
