def calculatorDisplay():
    
    display = """Welcome to Calculator
    
Choose one operation:
1. Add
2. Subtract
3. Exit
"""
    return(display)

# Function evelautes the conditions to verify the particular condition
def calculatorFunction(user_choice):
    if user_choice == 1:
        print("Let's perform addition")
        a, b = user_input()
        output = addition(a, b)
        return f"The sum is: {output}"
    elif user_choice == 2:
        print("Let's perform subtraction")
        a, b = user_input()
        output = subtraction(a, b)
        return f"The difference is: {output}"
    
    elif user_choice == 3:
        return "Exiting the calculator, bye bye!"

    else:
        return "Invalid choice. Please select 1, 2, or 3."
    
# Function takes user inputs and returns the values
def user_input():
    print("Give two numbers on two lines")
    a = int(input("Number 1 is: "))
    b = int(input("Number 2 is: "))
    return a, b

# Function to perform addition
def addition(a, b):
    return(a + b)


# Function to perform subtraction
def subtraction(a, b):
    return(a - b)

# Calls all functions and produce final results
while True:
    print(calculatorDisplay())
    user_choice = int(input("Select the operation: "))
    value = calculatorFunction(user_choice)
    print(value)

    if user_choice == 3:
        break