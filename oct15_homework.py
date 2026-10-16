def gmail_valid():
    username = input("enter username:")
    password = input("enter password:")
    email = input("enter email:")
    if len(username) > 3:
        if len(password) >= 8 and any(char.isdigit() for char in password):
            if '@' in email:
                print("You entered detatils are valid")
            else:
                print("Please add special symbol in email")
        else:
            print("please enter different password")
    else:
        print("Please check username length")
gmail_valid()