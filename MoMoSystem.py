#User
dial = input("Enter MoMo dialer: ")
MTNphone_number = "0782440907"
Airtelphone_number = "0755440179"
if dial == "*185#":
    print("1. Send Money\n" "2. Withdraw Money")
else:
    print("UNKOWN APPLICATION")
    exit()
choice = input("Select Choice: ")
if choice == "1":
    print("Send Money")
    print("1. MTN User")
    print("2. Airtel User")
    user = input("Select Mobile user: ")
    if user == "1":
        MTN_number = input("Enter MTN Number that that you are sending to: ")
        if MTN_number == MTNphone_number:
            Amount = int(input("Enter Amount: "))
            if Amount >= 500:
                pin = int(input("Enter your MoMo PIN to contiue: "))
                if pin > 2021:
                    print(str(Amount) + " has been sent to " + str(MTNphone_number))
                else:
                    print("Wrong PIN please check your PIN Again")
                    exit()
            else:
                print("Please enter Amount above 500/=")
                exit()
        else:
            print("Wrong Number, Please check number again!")
            exit()
    elif user == "2":
        Airtel_number = input("Enter Airtel Number that that you are sending to: ")
        if Airtel_number == Airtelphone_number:
            Amount = int(input("Enter Amount: "))
            if Amount >= 500:
                pin = int(input("Enter your Airtel Money PIN to contiue: "))
                if pin > 256:
                    print(str(Amount) + " has been sent to " + str(Airtelphone_number))
                else:
                    print("Wrong PIN please check your PIN Again")
                    exit()
            else:
                print("Please enter Amount above 500/=")
                exit()
        else:
            print("Wrong Number, Please check number again!")
            exit()
    else:
        print("UNKOWN APPLICATION")
        exit()
elif choice == "2":
    print("Withdraw Money")
else:
    print("UNKOWN APPLICATION")
