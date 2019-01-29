  # Items up here .......

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


if __name__ == '__main__':
    unittest.main()