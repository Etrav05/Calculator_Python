
def multiply(x, y):
    return float(x) * float(y)

def divide(x, y):
    return float(x) / float(y)

def add(x, y):
    return float(x) + float(y)

def sub(x, y):
    return float(x) - float(y)

def processBrackets(input_list):  # process the ( ) operators first and their contents ("B" EDMAS)
    i = 0
    stack = []  # store initial bracket "("
    while i < len(input_list):
        if input_list[i] == "(":
            stack.append(i)
        elif input_list[i] == ")":
            if not stack:
                raise ValueError("Mismatched parentheses: found ')' without a matching '('")  # error handling
            start = stack.pop()  # start from the first element
            result = processAddSub(processMultDiv(input_list[start + 1:i]))
            input_list[start:i + 1] = [str(result[0])]  # result is a list, so take the first element
            i = start  # reset index to handle new length
        i += 1
    if stack:
        raise ValueError("Mismatched parentheses: found '(' without a matching ')'")
def processMultDiv(input_list):  # process the * and / operators (BE "DM" AS)
    i = 0
    while i < len(input_list):
        if input_list[i] == "*":
            result = multiply(input_list[i - 1], input_list[i + 1])  # do calculation
            input_list[i - 1:i + 2] = [str(result)]  # replace operator and operands
            i = 0  # reset index to function with new input_list length
        elif input_list[i] == "/":
            result = divide(input_list[i - 1], input_list[i + 1])
            input_list[i - 1:i + 2] = [str(result)]
            i = 0
        else:
            i += 1
    return [eval("".join(input_list))]

def processAddSub(input_list):  # process the + and - operators (BEDM "AS")
    i = 0
    while i < len(input_list):
        if input_list[i] == "+":
            result = add(input_list[i - 1], input_list[i + 1])  # do calculation
            input_list[i - 1:i + 2] = [str(result)]  # replace operator and operands
            i = 0  # reset index to function with new input_list length
        elif input_list[i] == "-":
            result = sub(input_list[i - 1], input_list[i + 1])
            input_list[i - 1:i + 2] = [str(result)]
            i = 0
        else:
            i += 1
    return [eval("".join(input_list))]

userInput = [i for i in input('Enter function here (*, /, -, +, accepted): ').split()]  # takes input -> splits elements

input_list = list(userInput)  # the list of all elements inputted

result = processBrackets(processAddSub(processMultDiv(input_list)))

for i in input_list:
  print(i)
