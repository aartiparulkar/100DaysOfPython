def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("Enter the first number: "))
    calculating = True
    
    while calculating:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))
        
        result = operations[operation](num1, num2)
        
        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue with {result}. Type 'n' to start new calculation. ")
        if choice == 'y':
            num1 = result

        else:
            calculating = False
            print("\n" * 20)
            calculator()

calculator()
