## Password Locker
## Author
Loise Mwarangu (https://github.com/LoiseMwarangu)

# Description
This is a terminal based python program that allows its users to store their various accounts' credentials.These include account name,account username and password.The program also generates new passwords at the request of the user.

# Setup/Installation Requirements
To start using this project use the following commands:

* git clone https://github.com/LoiseMwarangu/Password-Locker
* cd PasswordLocker
* atom .
* code . (this is if Visual Studio Code is your preferred text editor)
To run this program,run these command lines in your terminal:
* chmod +x run.py
* ./run.py
# Behavior Driven Development
The program should ask for user's username and password when ca(create account) is entered:

Input Example: Enter ca

Output Example: What is your username?

Output Example: What is your password?

The program should authenticate the account by asking the user to login again when cc(create credential) is entered:

Input Example: Enter cc

Output Example: Login to your account. Username?

The program should create credentials when cc(create credential) is entered:

Input Example: Enter cc

Output Example: Enter the account name

The program should generate a random 8 characters long password when gp(generate password) is entered:

Input Example: Enter gp

Output Example: Your password is: ht43iphw

The program should let the user create their own password when cp(create password) is entered:

Input Example: Enter cp

Output Example: Enter your password

The program should display the credentials when dc(display credentials) is entered:

Input Example: Enter dc

Output Example: Here is a list of all of your credentials...

The program should end when ex(exit program) is entered:

Input Example: Enter ex

Output Example: Thank you for using Password locker...
## License
MIT License

Copyright (c) 2019 LoiseMwarangu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.