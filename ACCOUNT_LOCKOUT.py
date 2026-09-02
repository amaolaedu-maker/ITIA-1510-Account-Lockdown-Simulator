
CORRECT_PASSWORD = 'PASSWORD1!'
MAX_ATTEMPTS = 3

counter = 0
password_success = False

while counter < MAX_ATTEMPTS:

    counter = counter + 1
    password = input('Please enter your password:')


    if password == CORRECT_PASSWORD:
        print("Access Granted!")
        password_success = True

        break

    else:
        print("Access Denied", MAX_ATTEMPTS - counter, " Attempts remaining.")
if password_success:
    print("ACCESS GRANTED:", counter)

    digits = 0
    for char in password:
        if char in "0123456789":
            digits = digits + 1
    print("Password length:", len(password), "Number of digits:", digits)
else:
    print("ACCOUT LOCKED:", counter)


    print("End of program")