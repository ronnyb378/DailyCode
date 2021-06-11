from App import app

# ? This code runs different routines when executed
# TODO how to run system commands within python
# TODO ability to close all apps after finishing my routine
# TODO there should be a routine for different things through out the day
# TODO make it universal so that anyone can use it 
# TODO need to make a READ ME 

# * create the menu for the routine
print('''
Welcome sir,
    what are we doing?

1) Daily
2) Coding
3) Exit
''')
des = input('Number: ')

if des == '1':
    #morning routine
    while True:
        print('''
1) School
2) After School
3) Resting
4) Social
        ''')
        des = input('Number: ')
        if des == '1':
            app.open_app('Safari')
            app.open_app('Slack')
            

        elif des == '2':
            app.open_app('Safari')
            app.open_app('Headspace')
            app.open_appSystem('Music')
            app.open_appSystem('Messages')
            app.open_appSystem('Stickies')


        elif des == '3':
            app.open_app('Safari')
            app.open_appSystem('Messages')
            app.open_appSystem('Music')

        elif des == '4':
            print('Get ya ass back to work')
