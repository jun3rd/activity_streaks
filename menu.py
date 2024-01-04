import logactivity
import json


choice = 0
filelength = ""
last_line = ""
START_ACTIVITY_STREAKS = "START Activity Streaks"
START_VALUE_INVESTING = "START Value Investing"
START_MASTER_PYTHON = "START Master Python"
STOP = "STOP"

def getCurrentActivity():
    global last_line
    last_line = str.strip(logactivity.getLastLine())
    print("current activity: ", last_line)

def showMenu():
    print("Activities:")
    print("(1) START coding python: activity streaks")
    print("(2) START coding python: value investing")
    print("(3) START learning python: master python")
    print("(4) STOP (any activity)")

def selectActivity():
    global choice
    choice = input("choose activity?")
    choice = int(choice)
    global last_line
    #getCurrentActivity()
    if (choice == 1 and last_line == STOP):
            logactivity.activityStreaks_logstart()
    elif (choice == 2 and last_line == STOP):
            logactivity.valueInvesting_logstart()
    elif (choice == 3 and last_line == STOP):
            logactivity.masterPython_logstart()
    elif (choice == 4 and (last_line == START_ACTIVITY_STREAKS or last_line == START_VALUE_INVESTING or last_line == START_MASTER_PYTHON)):
            logactivity.logstop()
    else:
        print("not an option")

def showActivities():
    logactivity.readlog()


showMenu()
getCurrentActivity()
selectActivity()
showActivities()

