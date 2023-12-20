import logactivity

choice = 0
filelength = ""
last_line = ""

def getLastLine():
    global last_line
    last_line = str.strip(logactivity.getLastLine())
    print("last_line: ", last_line)

def showMenu():
    print("Activities:")
    print("(1) START coding python: activity_streaks")
    print("(2) STOP coding python: activity_streaks")

def selectActivity():
    global choice
    choice = input("choose activity?")
    choice = int(choice)
    global last_line
    getLastLine()
    if (choice == 1 and last_line == "STOP"):
            logactivity.python_logstart()
    elif (choice == 2 and last_line == "START"):
            logactivity.python_logstop()
    else:
        print("not an option")

def showActivities():
    logactivity.readlog()


showMenu()
getLastLine()
selectActivity()
showActivities()

