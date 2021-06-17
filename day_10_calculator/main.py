from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": substract, 
    "*": multiply,
    "/": divide
}
print(logo)
def calculator():
    num1 = float(input("What's the first number?: "))
    
    continue_operation = True
    
    for symbol in operations:
        print(symbol)
    while continue_operation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        next_step = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculattion: \n").lower()
        if next_step == "y":
            num1 = answer
        elif next_step == "n":
            continue_operation = False
            calculator()

calculator()
