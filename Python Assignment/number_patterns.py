
    
#checking number properties
def check_number(n):
    print(f"\nAnalyzing number: {n}")

    # Check even or odd
    if n % 2 == 0:
        print("- It is EVEN")
    else:
        print("- It is ODD")

    # Check if multiple of 5
    if n % 5 == 0:
        print("- It is a multiple of 5")
    elif n % 3 == 0:
        print("- It is a multiple of 3")

    # Check if square number
    if int(n ** 0.5) ** 2 == n:
        print("- It is a PERFECT SQUARE")

    # Check prime
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("- It is NOT prime")
                break
        else:
            print("- It is a PRIME number")


# Run the script
while True:
    num = input("\nEnter a number (or 'exit' to quit): ")
    if num.lower() == "exit":
        print("Goodbye!")
        break
    elif num.isdigit():
        check_number(int(num))
    else:
        print("Please enter a valid number.")
