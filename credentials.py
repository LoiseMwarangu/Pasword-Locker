class credentials:

    """
    Class that generates new instances of credentials.
    """ 
    credentials_list = []

    def __init__(self,account_name,my_user_name,password):
        self.account_name = account_name
        self.user_name = my_user_name
        self.password = password
 

    credentials_list = [] # Empty credentials list
    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''
        credentials.credentials_list.append(self)

   


