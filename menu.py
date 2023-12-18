import logactivity

choice = 0

def showmenu():
    print("Activities:")
    print("(1) START coding python: activity_streaks")
    print("(2) END coding python: activity_streaks")

def select_activity():
    global choice
    choice = input("choose activity?")
    choice = int(choice)

showmenu()
select_activity()

if choice == 1:
    logactivity.logstart()
elif choice == 2:
    logactivity.logend()
else:
    print("not an option")


