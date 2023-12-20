import logactivity

filesize = logactivity.getFileLength()

print("filesize: ", filesize)

lastline = str.strip(logactivity.getLastLine())

wordSTOP = "STOP"

print("lastline value: ", lastline)
print("wordSTOP value: ", wordSTOP)
print("lastline type: ", type(lastline))
print("wordSTOP type: ", type(wordSTOP))
print("type(lastline) == type(wordSTOP): ", type(lastline) == type('STOP'))
print("lastline == wordSTOP: ", lastline == wordSTOP)
print("--------------------------------")
fruit1 = 'Apple'
print('match fruits: ', fruit1 == 'Apple')

