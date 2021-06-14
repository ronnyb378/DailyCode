from App import App


# ? This code runs different routines when executed
# TODO how to run system commands within python
# TODO ability to close all apps after finishing my routine
# TODO there should be a routine for different things through out the day
# TODO need to make a READ ME 

# TODO have it open the directory for school so that you can edit/use/open school files during school


#! These are all the apps that are being used in your code
#! Add apps by following the order format and find out where app is located
# ? these apps are for open_app
headspace = App('Headspace')
safari = App('Safari')
slack = App('Slack')
visualcode = App('Visual Studio Code')

# ? these apps are for open_appSystem
music = App('Music', True)
calendar = App('Calender', True)
launchpad = App('Launchpad', True)
messages = App('Messages', True)
notes = App('Notes', True)
stickies = App('Stickies', True)
stocks = App('Stocks', True)

# headspace.open_app()
# music.open_app()

# * create the menu for the routine
print('''
Welcome sir,
    what are we doing?

1) Daily
2) Coding
3) Exit
''')
des = input('Number: ')
# these following list is to keep track which application is in each path
if des == '1':
    #morning routine
    while True:
        print('''
0) Go back
1) School
2) After School
3) Resting
        ''')
        des = input('Number: ')
        if des == '1':
            safari.open_app()
            slack.open_app()
            # while True:
            #     print('''
            #     0) Go back
            #     1) Another App
            #     2) Close School Apps
            #     3) Break Time
            #     4) Coding Time
            #     ''')

        elif des == '2':
            safari.open_app()
            headspace.open_app()
            music.open_appSystem()
            messages.open_appSystem()
            stickies.open_appSystem()

        elif des == '3':
            safari.open_app()
            messages.open_appSystem()
            music.open_appSystem()

