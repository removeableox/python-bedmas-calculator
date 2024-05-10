def tokenize(equation):
    tokens = []
    operators = "+-/*()^"
    temp = ""

    for i in equation:
        if i in operators:
            if temp: tokens.append(int(temp))
            tokens.append(i)
            temp = ""
            continue
        temp += i
    if temp: tokens.append(int(temp))

    return tokens

def find_first(inp, item):
    for index, i in enumerate(inp):
        if i == item:
            return index
    return len(inp)-1

def e(equation):
    while "^" in equation:
        e = find_first(equation, "^")
        left = equation[e-1]
        right = equation[e+1]
        equation = equation[:e-1] + [left ** right] + equation[e+2:]
    return equation
 
def dm(equation):
    while "/" in equation or "*" in equation:
        div = find_first(equation, "/")
        mult = find_first(equation, "*")
        
        if div != -1 and (mult == -1 or div < mult):
            left = equation[div - 1]
            right = equation[div + 1]
            equation = equation[:div - 1] + [left / right] + equation[div + 2:]
        else:
            left = equation[mult - 1]
            right = equation[mult + 1]
            equation = equation[:mult - 1] + [left * right] + equation[mult + 2:]
            
    return equation

def ad(equation):
    while "+" in equation or "-" in equation:
        div = find_first(equation, "+")
        mult = find_first(equation, "-")
        
        if div != -1 and (mult == -1 or div < mult):
            left = equation[div - 1]
            right = equation[div + 1]
            equation = equation[:div - 1] + [left + right] + equation[div + 2:]
        else:
            left = equation[mult - 1]
            right = equation[mult + 1]
            equation = equation[:mult - 1] + [left - right] + equation[mult + 2:]
            
    return equation

def EDMAS(tokens):
    return ad(dm(e(tokens)))[0]

def parse_brackets(tokens):
    temp = 0
    starting_pos = 0
    new_tokens = []

    for index, i in enumerate(tokens):
        if i == '(':
            temp += 1
            if temp == 1:
                starting_pos = index
            continue

        if i == ')':
            temp -= 1
            if temp == 0:
                new_tokens.append(parse_brackets(tokens[starting_pos+1:index]))
                continue

        if temp == 0:
            new_tokens.append(i)

    return new_tokens

def BEDMAS(tokens):
    for index, i in enumerate(tokens):
        if type(i) == list:
            tokens[index] = BEDMAS(i)
    return EDMAS(tokens)

def evaluation(expression):
    return BEDMAS(parse_brackets(tokenize(expression)))

# example
print(evaluation("4+4^(5*5)"))
