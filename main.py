
from App import App
import os
# import colorama
# from colorama import Fore, Back, Style
# TODO need to make a READ ME 

#what did you learn
#show the code

# ? these apps are for open_app
headspace = App('Headspace')
safari = App('Safari')
slack = App('Slack')

# ? these apps are for open_app
music = App('Music', True)
calendar = App('Calender', True)
launchpad = App('Launchpad', True)
messages = App('Messages', True)
notes = App('Notes', True)
stickies = App('Stickies', True)
stocks = App('Stocks', True)
all_apps = [music, safari, calendar, messages, notes, stickies, stocks,
    headspace, safari, slack]
#  * create the menu for the routine
while True:
        print('''
1) School
2) After School
3) Resting
4) Close Apps
5) Exit\n''')
        des = input('Number: ')
        if des == '1':
            safari.open_app()
            slack.open_app()
            des = input('\nWant the launchpad?(y/n): ')
            if des == 'y':
                launchpad.open_app()             
            while True:
                print('''
0) Go back
1) Close School Apps
''')
                des = input('Number: ')
                if des == '0':
                    break
                elif des == '1':
                    #close apps 
                    safari.close_app()
                    slack.close_app()
                    break

        elif des == '2':
            safari.open_app()
            headspace.open_app()
            music.open_app()
            messages.open_app()
            stickies.open_app()
            while True:
                print('''
0) Go back
1) Close After School Apps''')
                des = input('\nNumber: ')
                if des == '0':
                    break
                elif des == '1':                    
                    #close apps 
                    safari.close_app()
                    headspace.close_app()
                    messages.close_app()
                    stickies.close_app()
                    break

        elif des == '3':
            safari.open_app()
            messages.open_app()
            music.open_app()
            while True:
                print('''
0) Go back
1) Close Resting Apps''')
                des = input('\nNumber: ')
                if des == '0':
                    break
                elif des == '1':
                    safari.close_app()
                    messages.close_app()
                    music.close_app()

        elif des == '4':

            while True:
                print('''
0) Go back
1) Any apps you don't want to close? 
2) Close All
                ''')
                des = input('\nNumber: ')
                if des == '1':
                    name_of_app = []
                    for app in all_apps:
                        title = app.app_name
                        print(title, end = ' | ')
                        name_of_app.append(title)
                        # print(name_of_app)
                    app_des = input('\nWhich app should I leave open?: ')
                    name_of_app.remove(app_des)
                    while True:
                        y0n = input('\nAny other app? (y/n): ')
                        if y0n == 'n':
                            for app in name_of_app:
                                os.system(f'killall {app}')
                            break
                        else:
                            app_des = input('\nWhat other app?: ')
                            name_of_app.remove(app_des)
                            continue
                elif  des == '2':            
                    for app in all_apps:
                        app.close_app()
                else: 
                    break
        elif des == '5':
            quit()