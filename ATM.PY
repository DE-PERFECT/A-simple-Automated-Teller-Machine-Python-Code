import random

print("Welcome to BestStar ATM")

option = input("Enter your option:\n1. Create an account\n2. Already have an account\n")

if option == "1":
    print("Please provide the following details to create your account:")
    first_name = input("First name:\n")
    last_name = input("Last name:\n")
    age = input("Age:\n")
    security_question = input("Maiden name , Pet name:\n")
    account_number = random.randint(1000000000, 9999999999)
    print(f"Congratulations {first_name} {last_name}! Your account has been successfully created with account number {account_number}.")
    pin = input("Please input a 4-digit PIN for your account:\n")
elif option == "2":
    print("Insert Your Atm Card:")
    pin = input("Please input your PIN:\n")
    # Assume the PIN and account number are valid and match a record in the database
    # Retrieve the first name and last name associated with the account number
    first_name = "John"
    last_name = "Doe"
    print(f"Welcome, {first_name} {last_name}!")
    
if len(pin) != 4 or not pin.isdigit():
    print("Invalid PIN. Please try again.")
else:
    pin = int(pin)
    print("PIN accepted.")
    enter = input("Press Click Enter to continue with your transaction.")
while True:
    print("Please select an option:")
    print("1. Check account balance")
    print("2. Transfer money")
    print("3. Withdraw money")
    print("4. Deposit money")
    print("5. Change PIN")
    print("6. Exit")
    option = input("Enter option number (1-6): ")
    
    if option == "1":
        print("Your account balance is $2000.")
    elif option == "2":
          print("List of available banks:")     
          print("1. Bobo Bank")
          print("2. Best Star Merchant Saving Bank")
          print("3. Omin Bank")
          print("4. Best Star Tuition Bank")
          bank = input("Enter the bank you want to transfer money to: ")
          account_num = input("Enter the beneficiary account number: ")
          if bank not in ["1", "2", "3", "4"]:
              print("Invalid bank number. Please try again.")                    
          else:
              amount = input("Enter the amount you want to transfer: ")
              print(f"You have succesfully transferred ${amount} to bank {account_num}")
              
    elif option == "3":
        amount = int(input("Enter the amount to withdraw:\n"))
        if amount <= 0:
            print("Invalid amount. Please try again.")
        elif amount > 2000:
                print("Insufficient funds. Please try again.")
        else:
                print("Please take your cash.")
                print("Remaining balance is $", 2000-amount)
                
    elif option == "4":
         # deposit money
         amount = int(input("Enter amount to deposit: "))
         if amount <= 0:
             print("Invalid amount. Please try again.")
         else:
                print("Your deposit of $", amount, "is successful.")
                print("Updated balance is $", 2000+amount)


                
    elif option == "5":
        new_pin = input("Enter your new 4-digit PIN:\n")
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("Invalid PIN. Please try again.")
        else:
            pin = int(new_pin)
            print("PIN changed successfully.")
            pin = new_pin

            
    elif option == "6":
        print("Thank you for using BestStar ATM. Goodbye")
        break
    
    else:
        print("Invalid option. Please try again.")
    
print
