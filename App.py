import os 

class app:
    def __init__(self, app):
        self.app = app

    #? os acts like a terminal, in () is what is inserted to the makeshift terminal
    #? this is a path to first half of all applications 
    def open_appSystem(self):
            os.system(f'open /System/Applications/{self}.app')

    #? this is another path to the second half of applications         
    def open_app(self):
            os.system(f'open /Applications/{self}.app')

    #? this is to close any application
    def close(self):
        os.close(f'{self}')
