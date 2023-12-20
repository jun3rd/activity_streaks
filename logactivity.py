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

def python_logstart():
    x = datetime.datetime.now()
    x = str(x)
    f = open(currentfile, "a")
    f.write("START\n")
    f.write(x)
    f.write("\n")
    f.close()

def python_logstop():
    x = datetime.datetime.now()
    x = str(x)
    f = open(currentfile, "a")
    f.write("STOP\n")
    f.write(x)
    f.write("\n")
    f.close()

