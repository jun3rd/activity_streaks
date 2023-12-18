import datetime

def readlog():
    f = open("activites.csv", "r")
    print(f.read())

def logstart():
    x = datetime.datetime.now()
    x = str(x)
    f = open("activities.csv", "a")
    f.write("start\n")
    f.write(x)
    f.write("\n")
    f.close()

def logend():
    x = datetime.datetime.now()
    x = str(x)
    f = open("activities.csv", "a")
    f.write("end\n")
    f.write(x)
    f.write("\n")
    f.close()

