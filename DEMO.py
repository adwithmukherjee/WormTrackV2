from main import trackerMain
from HelpFxns import vidToImage2

#This is the main script to run the entire tracker on a video file in terminal 
# John ~1 hour


filepath= input('Input video set filepath: ') # use vid7.avi for testing
method= int(input('Choose tracking type: \n1: Basic Tracker\n2: New Tracker (No Neural Net) \n3: New Tracker w/ Neural Net\nYour Choice: ')) 
frameSkip= int(input('How many frames between position checks?: ')) #frame skip of 5 to 25 makes the tracker run faster and track more accurately
# print(filepath)
# print(method)
# print(frameSkip)
outImgFolder= 'frames'
vidToImage2(filepath, outImgFolder)


trackerMain(outImgFolder,method,frameSkip)