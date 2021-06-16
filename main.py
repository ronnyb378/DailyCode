
from app import App
import os
# TODO need to make a READ ME 

headspace = App('Headspace')
safari = App('Safari')
slack = App('Slack')
music = App('Music', True)
calendar = App('Calender', True)
launchpad = App('Launchpad', True)
messages = App('Messages', True)
notes = App('Notes', True)
stickies = App('Stickies', True)
stocks = App('Stocks', True)

all_apps = [music, safari, calendar, messages, notes,
stickies, stocks, headspace, safari, slack]

while True:
        print('\033[32m' + '''
1) School
2) After School
3) Resting
4) Close Apps''' + '\033[39')
        print('\033[4;31m' + '5) Exit\n' + '\033[0;39m')
        des = input('Number: ')
        if des == '1':
            yay0nay = input('\033[32m' + '\nOpen apps? (y/n): '+'\033[0;39m')
            if yay0nay == 'y':
                safari.open_app()
                slack.open_app()
            des = input('\033[32m'+'\nWant the launchpad?(y/n): ')
            if des == 'y':
                launchpad.open_app()             
            while True:
                print('\033[32m'+'\n0) Go back')
                print('\033[31m'+"1) Any apps you don't want to close?")
                print('\033[4;31m'+'2) Close School Apps' + '\033[0;39m')
                des = input('\033[0;39m'+'\nNumber: ')
                print(' ')
                if des == '0':
                    break
                elif des == '1':
                    name_of_app = []
                    print(' ')
                    for app in all_apps:
                        title = app.app_name
                        print('\033[33m'+title, end = ' | ' + '\033[0;39m')
                        name_of_app.append(title)
                    app_des = input('\033[36m'+'\nWhich app should I leave open?: '+ '\033[0;39m')
                    name_of_app.remove(app_des)
                    while True:
                        print()
                        y0n = input('\033[32m'+'Any other app? (y/n): '+ '\033[0;39m')
                        if y0n == 'n':
                            for app in name_of_app:
                                os.system(f'killall {app}')
                            break
                        else:
                            app_des = input('\nWhat other app?: ')
                            name_of_app.remove(app_des)
                            continue
                elif des == '2':
                    #close apps 
                    safari.close_app()
                    slack.close_app()
                    break
        elif des == '2':
            yay0nay = input('\033[32m' + '\nOpen apps? (y/n): '+'\033[0;39m')
            if yay0nay == 'y':
                safari.open_app()
                headspace.open_app()
                music.open_app()
                messages.open_app()
                stickies.open_app()
            while True:
                print('\033[32m'+'\n0) Go back')
                print('\033[31m'+"1) Any apps you don't want to close?")
                print('\033[4;31m'+'2) Close After School Apps' + '\033[0;39m')
                des = input('\033[0;39m'+'\nNumber: ')
                if des == '0':
                    break
                if des == '1':
                    name_of_app = []
                    print(' ')
                    for app in all_apps:
                        title = app.app_name
                        print('\033[33m'+title, end = ' | ' + '\033[0;39m')
                        name_of_app.append(title)
                    app_des = input('\033[36m'+'\nWhich app should I leave open?: '+ '\033[0;39m')
                    name_of_app.remove(app_des)
                    while True:
                        print()
                        y0n = input('\033[32m'+'\nAny other app? (y/n): '+ '\033[0;39m')
                        if y0n == 'n':
                            for app in name_of_app:
                                os.system(f'killall {app}')
                            break
                        else:
                            app_des = input('\nWhat other app?: ')
                            name_of_app.remove(app_des)
                            continue
                elif des == '2':                    
                    #close apps 
                    safari.close_app()
                    headspace.close_app()
                    messages.close_app()
                    stickies.close_app()
                    break
        elif des == '3':
            yay0nay = input('\033[32m' + '\nOpen apps? (y/n): '+'\033[0;39m')
            if yay0nay == 'y':
                safari.open_app()
                messages.open_app()
                music.open_app()
            while True:
                print('\033[32m'+'\n0) Go back')
                print('\033[31m'+"1) Any apps you don't want to close?")
                print('\033[4;31m'+'2) Close Resting Apps' + '\033[0;39m')
                des = input('\033[0;39m'+'\nNumber: ')
                if des == '0':
                    break
                if des == '1':
                    name_of_app = []
                    print(' ')
                    for app in all_apps:
                        title = app.app_name
                        print('\033[33m'+title, end = ' | ' + '\033[0;39m')
                        name_of_app.append(title)
                    app_des = input('\033[36m'+'\nWhich app should I leave open?: '+ '\033[0;39m')
                    name_of_app.remove(app_des)
                    while True:
                        print()
                        y0n = input('\033[32m'+'Any other app? (y/n): '+ '\033[0;39m')
                        if y0n == 'n':
                            for app in name_of_app:
                                os.system(f'killall {app}')
                            break
                        else:
                            app_des = input('\nWhat other app?: ')
                            name_of_app.remove(app_des)
                            continue
                elif des == '2':
                    safari.close_app()
                    messages.close_app()
                    music.close_app()
        elif des == '4':
            while True:
                print('\033[32m'+'\n0) Go back')
                print('\033[31m'+"1) Any apps you don't want to close?")
                print('\033[1;4;31m'+'2) Close All' + '\033[0;39m')
                des = input('\nNumber: ')
                if des == '1':
                    name_of_app = []
                    print(' ')
                    for app in all_apps:
                        title = app.app_name
                        print('\033[33m'+title, end = ' | ' + '\033[0;39m')
                        name_of_app.append(title)
                    app_des = input('\033[36m'+'\nWhich app should I leave open?: '+ '\033[0;39m')
                    name_of_app.remove(app_des)
                    while True:
                        print()
                        y0n = input('\033[32m'+'Any other app? (y/n): '+ '\033[0;39m')
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