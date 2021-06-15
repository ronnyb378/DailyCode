
from App import App


# how to run system commands within python
# ability to close all apps after finishing my routine
# TODO there should be a routine for different things through out the day
# TODO need to make a READ ME 
# ! TODO tell me which apps where open and closed
# TODO have it open the directory for school so that you can edit/use/open school files during school

#! These are all the apps that are being used in your code
#! Add apps by following the order format and find out where app is located
# ? these apps are for open_app
# todo add Terminal to the list
# todo add Visual Studio Code
headspace = App('Headspace')
safari = App('Safari')
slack = App('Slack')

# ? these apps are for open_appSystem
all_apps = ['Music', 'Calendar', 'Launchpad', 'Messages', 'Notes', 'Stickies', 'Stocks']
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
                # TODO trying to let user open any app
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
                    continue
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
                continue
            elif des == '1':
                #close apps
                safari.close_app()
                messages.close_appSystem()
                # music.close_appSystem()

        elif des == '4':
            # todo (close specific or all apps)
            #! THIS NEEDS FIXING

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
                        print(app.app_name, end = '|')
                    # dont_close = input("\nDon't close: ")
                    # all_apps.remove(dont_close)
                    # print(all_apps)
                elif  des == '2':            
                    for app in all_apps:
                        app.close_app()

        else: 
            break