import random
from user import User
from credentials import Credential

def create_user_account(user_name,pass_word):
    """
    Function to create a new account
    """
    new_user = User(user_name,pass_word)
    return new_user

def create_credentials(view_password,account,login_name,pass_word):
    """
    Function to create a new credential
    """
    new_credential = Credential(view_password,account,login_name,pass_word)
    return new_credential

def save_user_account(user):
    """
    Function to save user account
    """
    user.save_user()

def save_credentials(credential):
    """
    Function to save credentials
    """
    credential.save_credential()

def check_existing_users(characters):
    """
    Function that checks if a user exists with those characters and retuen a boolean
    """
    return User.user_exists(characters)

def display_credentials():
     """
     Function that returns the credentials list
     """
     return Credential.display_credentials()
def main():
    print("Hello! Welcome to the Password Locker. please enter your name")
    u_name = input()
    print("\n")
    print(f"Hello {u_name}.")
    while True:
        print("\nUse these short codes below:")
        print("." * 40)
        print("\n ca - create an account, cc - create credentials, gp - generate password, cp - create own password, ex - exit password locker, dc - display credentials")
        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("." * 14)

            print("\nEnter your user name")
            print("."*40)
            user_name = input()

            print("\nEnter a password")
            print("."*40)
            pass_word = input()

            save_user_account(create_user_account(user_name,pass_word))

            print("\n")
            print(f"New Account **{user_name}** created.\n")

