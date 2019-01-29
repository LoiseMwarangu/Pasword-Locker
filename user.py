print("Hello there, welcome to password locker")
print()

userUsername= input("Enter your username:")
userPassword= input("Enter your password:")

while username != userUsername or password != userPassword:
    print("you entered a wrong username and/or password")
    userUsername= input("Enter your username:")
    userPassword= input("Enter your password:")

print("You are now logged in")




