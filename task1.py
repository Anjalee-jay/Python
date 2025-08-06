while True:
    try:
       
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

       
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")

      
        choice = input("Do you want to add more numbers? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exit")
            break

    except ValueError:
        print("Invalid input. Please enter numeric values.")
