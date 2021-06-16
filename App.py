import os 

opened_System = []
opened = []

class App:
    def __init__(self, app_name, system_app= False):
        self.app_name = app_name
        self.system_app = system_app

    def open_appSystem(self):
        os.system(f"open /System/Applications/{self.app_name}.app")
        opened_System.append(f'{self.app_name}')
        return opened_System

    def open_app(self):
        if self.system_app:
            self.open_appSystem()
        else:
            os.system(f'open /Applications/{self.app_name}.app')
            opened.append(f'{self.app_name}')
            return opened

    def close_app(self):
            os.system(f"killall {self.app_name}")
    

