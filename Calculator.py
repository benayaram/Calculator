print("--- Welcome to Calculator ---")
print("Enter a calculation using numbers and operators (+, -, *, /).")
print("Type 'exit' to quit.")
print("-" * 30)

ALLOWED_CHARS = "0123456789.+-*/() "

while True:
    expression = input("Calculate: ")
    if expression.lower() == 'exit':
        break

    is_valid = True 
    for char in expression:

        if char not in ALLOWED_CHARS:
            is_valid = False
            break
    if is_valid:
        try:
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: Invalid expression. \nDetails: {e}")
    else:
        print(f"Error: Invalid characters found. Please only use numbers and math operators.")

    print("-" * 30)

print("--- Calculator closed! ---")
