from main import trackerMain
from HelpFxns import vidToImage2

filepath= input('Input video set filepath: ')
method= int(input('Choose tracking type: \n1: Basic Tracker\n2: New Tracker (No Neural Net) \n3: New Tracker w/ Neural Net\nYour Choice: '))
frameSkip= int(input('How many frames between position checks?: '))
# print(filepath)
# print(method)
# print(frameSkip)
outImgFolder= 'frames'
vidToImage2(filepath, outImgFolder)


trackerMain(outImgFolder,method,frameSkip)