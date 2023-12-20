import datetime
import os

currentfile = "activities.csv"

def getFileLength():
    path = currentfile
    size = os.path.getsize(path)
    return size

def getLastLine():
    f = open(currentfile, "r")
    last_line = f.readlines()[-2]
    return last_line

def readlog():
    f = open(currentfile, "r")
    print(f.read())

def activityStreaks_logstart():
    x = datetime.datetime.now()
    x = str(x)
    f = open(currentfile, "a")
    f.write("START Activity Streaks\n")
    f.write(x)
    f.write("\n")
    f.close()

def valueInvesting_logstart():
    x = datetime.datetime.now()
    x = str(x)
    f = open(currentfile, "a")
    f.write("START Value Investing\n")
    f.write(x)
    f.write("\n")
    f.close()

def masterPython_logstart():
    x = datetime.datetime.now()
    x = str(x)
    f = open(currentfile, "a")
    f.write("START Master Python\n")
    f.write(x)
    f.write("\n")
    f.close()

def logstop():
    x = datetime.datetime.now()
    x = str(x)
    f = open(currentfile, "a")
    f.write("STOP\n")
    f.write(x)
    f.write("\n")
    f.close()


