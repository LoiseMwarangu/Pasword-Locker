class credentials:

    """
    Class that generates new instances of credentials.
    """ 
    credentials_list = []

    def __init__(self,account_name,my_username,password):
        self.account_name = account_name
        self.user_name = my_username
        self.password = password
 

    credentials_list = [] 
    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''
        credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_list
    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        credentials.credentials_list.remove(self)
    @classmethod
    def find_by_number(cls,passwor:
        '''
        Method that takes in a password and returns a credentials that matches that password.

        Args:
            password: password to search for
        Returns :
            credentials of person that matches the password.
        '''

        for credentials in cls.credentials_list:
            if credentials.password == passwor:
                return credentials