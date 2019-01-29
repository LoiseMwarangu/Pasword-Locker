import unittest # Importing the unittest module
from credentials import credentials # Importing the credentials class

class Testcredentials(unittest.TestCase):


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = credentials("facebook","loise","lo15e") # create credentials object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name,"facebook")
        self.assertEqual(self.new_credentials.my_user_name,"loise")
        self.assertEqual(self.new_credentials.password,"lo15e")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(credentials.credentials_list),1)
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = credentials("Test","user","loise","test@user.com") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(credentials.credentials_list),2)
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = credentials("Test","user","0712345678","test@user.com") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(credentials.credentials_list),2)

    if __name__ == '__main__':
        unittest.main()

    