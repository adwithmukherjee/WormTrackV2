from main import trackerMain

filepath= input('Input image set filepath: ')
method= int(input('Choose tracking type: \n1: Basic Tracker\n2: New Tracker (No Neural Net) \n3: New Tracker w/ Neural Net\nYour Choice: '))
frameSkip= int(input('How many frames between position checks?: '))
# print(filepath)
# print(method)
# print(frameSkip)


trackerMain(filepath,method,frameSkip)