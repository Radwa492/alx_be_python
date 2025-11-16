first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = 0  
match operation:
    case "+":  
        result = first_number + second_number
        print(f"the result is: {result}")
    case "-":
        result = first_number - second_number
        print(f"the result is: {result}")               
    case "*":
        result = first_number * second_number
        print(f"the result is: {result}")
    case "/":
        if second_number != 0:
            result = first_number / second_number
            print(f"the result is: {result}")    
        else:
            print("Cannot divide by zero.")  
