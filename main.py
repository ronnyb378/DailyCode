
from App import App
import os
# TODO need to make a READ ME 

# ? these apps are for open_app
headspace = App('Headspace')
safari = App('Safari')
slack = App('Slack')

# ? these apps are for open_appSystem
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
5) Exit
        ''')
        des = input('Number: ')
        if des == '1':
            safari.open_app()
            slack.open_app()
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
            music.open_appSystem()
            messages.open_appSystem()
            stickies.open_appSystem()
            while True:
                print('''
0) Go back
1) Close After School Apps''')
                des = input('Number: ')
                if des == '0':
                    break
                elif des == '1':                    
                    #close apps 
                    safari.close_app()
                    headspace.close_app()
                    messages.close_appSystem()
                    stickies.close_appSystem()
                    break

        elif des == '3':
            safari.open_app()
            messages.open_appSystem()
            music.open_appSystem()
            print('''
0) Go back
1) Close Resting Apps''')
            des = input('Number: ')
            if des == '0':
                break
            elif des == '1':
                safari.close_app()
                messages.close_appSystem()
                music.close_appSystem()

        elif des == '4':

            while True:
                print('''
0) Go back
1) Any apps you don't want to close? 
2) Close All
                ''')
                des = input('Number: ')
                if des == '1':
                    print('Which app should I leave open?')
                    for app in all_apps:
                        title = app.app_name
                        print(title, end = ' | ')
                    x = 0
                    name_of_app = []
                    if x < len(all_apps):
                        for app in all_apps:
                            app_name = app.app_name
                            name_of_app.append(app_name)                      
                        x += 1
                    # print(name_of_app)
                    close = input('\nWhich app to leave open?: ')
                    name_of_app.remove(close)
                    for app in name_of_app:
                        os.system(f'killall {app}')

                elif  des == '2':            
                    for app in all_apps:
                        app.close_app()

                else: 
                    break
        else: 
            break