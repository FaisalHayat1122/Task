print("====== Welcome to Faisal's Simple Program ======")

while True:
    print("\nChoose an option:")
    print("1. Check Even or Odd")
    print("2. Check Positive, Negative, or Zero")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

    elif choice == 2:
        num = int(input("Enter a number: "))
        if num > 0:
            print("Number is Positive")
        elif num < 0:
            print("Number is Negative")
        else:
            print("Number is Zero")

    elif choice == 3:
        print("Thank you! Program exited 👋")
        break

    else:
        print("Invalid choice! Please try again.")
        




