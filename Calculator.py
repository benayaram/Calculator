print("--- Welcome to Calculator ---")
print("Enter a full calculation (e.g., 5 * (10 + 2) / 3)")
print("Type 'exit' to quit.")
print("-" * 30)

while True:
    expression = input("Calculate: ")
    if expression.lower() == 'exit':
        break
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: Invalid expression. \nDetails: {e}")
    print("-" * 30) 

print("--- Calculator closed! ---")