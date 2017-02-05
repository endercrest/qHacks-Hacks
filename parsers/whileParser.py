
def whileparse(raw):
    """

    :param raw:
    :return:
    """
    lom = [{"Value": "while", "Type": "loop"}]
    # Does while get passed to me??
    raw = raw[5:]  # Strips while

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

    print(expression)

    # TODO Bool Expression Evaluations

    return lom

whileparse("while (x == 1):")
whileparse("while (x == 1)")
whileparse("while(x == 1)")
whileparse("while(x==1)")
whileparse("while x == 1")
whileparse("while x == 1:")
