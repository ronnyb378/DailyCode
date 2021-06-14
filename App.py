import os 

opened_System = []
opened = []

class App:
    def __init__(self, app_name, system_app= False):
        self.app_name = app_name
        self.system_app = system_app

    #? os acts like a terminal, in () is what is inserted to the makeshift terminal
    #? this is a path to first half of all applications 
    def open_appSystem(self):
        
        os.system(f'open /System/Applications/{self.app_name}.app')
        opened_System.append(f'{self.app_name}')
        #code works all the way till here
        return opened_System

    #? this is another path to the second half of applications         
    def open_app(self):
        if self.system_app:
            self.open_appSystem()
        else:
            
            os.system(f'open /Applications/{self.app_name}.app')
            opened.append(f'{self.app_name}')
            print(opened)
            return opened

    # #? this is to close any application
    # def close_appSystem(self):
    #     os.close(f'open /System/Applications/{self}.app')

    # #?this is another path to the second half of applications
    # def close_app(self):
    #     for names in opened: 
    #         os.system(f'''osascript -e "quit app '{names}'"''')