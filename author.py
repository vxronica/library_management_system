class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    #getter for name
    def get_name(self):
        return self.__name

    #setter for name
    def set_name(self, name):
        self.__name = name
    
    #gets biography
    def get_biography(self):
        return self.__biography
    
    #sets biogrpahy
    def set_biography(self, biography):
        self.__biography = biography