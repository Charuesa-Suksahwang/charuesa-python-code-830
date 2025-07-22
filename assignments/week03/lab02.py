# Complete this ATM simulation
balance = 1000
pin = "1234"
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            print("Your balance =",balance)
        elif choice == "2":
            amount = float(input("Widraw amount: "))
            if amount < 0:
                print("Cannot withdraw less than 0")
            else:
            balance = balance - amount
            print("Please collect your money, adn you balance now =",balance)
        if: choice == "3":
            amount = float(input("Deposit amouth:"))
            if amount < 0:
                print("Cannot withdraw less than 0")
            else:
                balance = balance + amount
                print("Your balance now",balance)
        if choice == "4":
            break
        else:
            print("Please select 1-4 only!!")
            continue
else:
    print("Invalid PIN")