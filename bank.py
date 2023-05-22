accounts = {
    "8309733623":"0963",
    "9704122623":"2233",
    "8297518502":"0143"}
customer_data={
    "ravi":"10000",
    "rajesh":"20000",
    "kiran":"30000"
}

customer_Names=[]
customer_dob=[]
customer_Pins=[]

print("=*20")

while True:
    print("----- WELCOME TO THE STATE BANK OF INDIA-----")
    print("*********************************************")
    print("<<<--- 1. Open a New Account --->>>")
    print("<<<--- 2. Withdraw Money --->>>")
    print("<<<--- 3. Deposit Money --->>>")
    print("<<<--- 4. check customerNames and balance")
    print("<<<--- 5. Close the Account --->>>")
    print("<<<--- 6. Exit/Quit--->>>")
    print("**********************************************")
    
    
    option = input("Please Enter Your Choice From Above Options")

    if option=="1":
        print("Thanks for showing intrest to open an account in our Bank")
        name=(input("Enter Your Name"))
        dob=(input("Enter your Date Of Birth"))
        pin=(input("Please set your pin number"))
        customer_Names.append(name)
        customer_dob.append(dob)
        customer_Pins.append(pin)
        print(" Your name and pin had sucessfully registered in our Bank account created sucessfully")

    
    elif option=="2":
        balance = 10000.0 # or any other starting balance
        account_number = input("Please enter your account number: ")
        pin = accounts.get(account_number)
        if pin:
            entered_pin = input("Please enter your PIN: ")
            if entered_pin == pin:
                print("PIN accepted")
            else:
                print("Invalid PIN")
        else:
            print("Invalid account number")

        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
        if withdrawal_amount > balance:
            print("Error: Insufficient balance")
            exit()
        balance -= withdrawal_amount
        print("New balance: ", balance)

    elif option=="3":
        balance = 10000.0 # or any other starting balance
        account_number = input("Please enter your account number: ")
        pin = accounts.get(account_number)
        if pin:
            entered_pin = input("Please enter your PIN: ")
            if entered_pin == pin:
                print("PIN accepted")
            else:
                print("Invalid PIN")
        else:
            print("Invalid account number")
        deposit_amount = float(input("Enter the amount you want to deposit: "))
        if deposit_amount < 0:
            print("Error: Invalid deposit amount")
            exit()
        elif deposit_amount == 0:
            print("Error: Deposit amount cannot be zero")
            exit()
        else:
            balance += deposit_amount
            print("New balance: ", balance)
        
    elif option == "4":
        # Prompt the user to enter a customer name
        customer_name = input("Enter a customer name: ")

        # Check if the customer name is in the dictionary
        if customer_name in customer_data:
            # If the customer name is in the dictionary, print their balance
            print("Customer", customer_name, "has a balance of", customer_data[customer_name])
        else:
            # If the customer name is not in the dictionary, print an error message
            print("Customer", customer_name, "was not found in the database")
            
    elif option =="5":
        # Prompt the user to enter a customer name
        customer_name = input("Enter a customer name: ")

        # Check if the customer name is in the dictionary
        if customer_name in customer_data:
        # If the customer name is in the dictionary, remove their entry from the dictionary
            del customer_data[customer_name]
            print("Customer", customer_name, "has been deleted from the database")
        else:
            # If the customer name is not in the dictionary, print an error message
            print("Customer", customer_name, "was not found in the database")

        
    elif option=="6":
        print("Thank You For Using State Bank Of India Services")  
        break 
    
    else:
        print("invalid responce please try again ")  
    



    
    

    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            