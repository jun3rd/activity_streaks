import logactivity

choice = 0
filelength = 0
last_line = ""

def getFileLength():
    global filelength
    filelength = logactivity.getFileLength()
    print("filelength: ", filelength)

def getLastLine():
    global last_line
    last_line = logactivity.getLastLine()
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
    if (choice == 1 and last_line == "STOP"):
            logactivity.python_logstart()
    elif (choice == 2 and last_line == "START"):
            logactivity.python_logstop()
    else:
        print("not an option")

def showActivities():
    logactivity.readlog()

def selectActivityTRY():
    global choice
    choice = input("choose activity?")
    choice = int(choice)
    global last_line
    last_line = str(last_line)
    print("last_line: ", last_line)
    print("last_line type: ", type(last_line))
    print("'STOP' type: ", type("STOP"))
    print("last_line == STOP: ", last_line == 'STOP')
    print("'WORD' == 'WORD': ", 'WORD' == 'WORD')


showMenu()
getFileLength()
getLastLine()
selectActivityTRY()
showActivities()

