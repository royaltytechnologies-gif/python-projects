bal = 10000
while True:
    print("1. Check account balance.")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input ("Choose an option:   ")
    if choice == "1":
        print(f"your Account Balance is ${bal}")
    elif choice == "2":
        amount=float(input("enter amount to deposit:   "))
        bal += amount
        print(f"Deposit successful. New Account balance is: ${bal}")
    elif choice == "3":
        amount = float(input("Enter the amount you want to  withdraw:   "))
        if amount >  bal:
            print ("Insufficient funds.  ")
        else:
            bal -= amount
            print(f"Withdrawal Successful. New Account balance is {bal}")
    elif choice == "4":
        print ("Thank you for banking with us.  ")
        break
    else:
        print("invalid option, try again.  ")