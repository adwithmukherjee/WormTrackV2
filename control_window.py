
## TO DO
# 1. create a window
# 2. input field for filepath, direct to run john's functions
# 3. check boxes for neural net or difference tracker
# 4. check for showing tracker
from psychopy import gui

from HelpFxns import ImgArray, folderToImgArray, getPosList

#title dialog box
myDlg = gui.Dlg(title="WORMS WORMS WORMS")

myDlg.addText('Control Settings')

#input a video file to track
myDlg.addField('Filepath:')

#input sensitivity value
myDlg.addField('Sensitivity:', 21)

#check box for show tracker or nah
myDlg.addField('Show tracker:', initial=False)

#choose to use neural net or difference tracker
myDlg.addField('Tracker type:', choices=["Neural Net", "Difference Tracker"])
ok_data = myDlg.show()  # show dialog and wait for OK or Cancel

if myDlg.OK:  # or if ok_data is not None

    #label data appropriately
    filepath = ok_data[0]
    sensitivity = ok_data[1]
    show_tracker = ok_data[2]
    nn_or_dt = ok_data[3]

    print(filepath)

    #direct to turn filepath into frames
    imgs = folderToImgArray(filepath)
    if nn_or_dt == 'Difference Tracker':
        positions = getPosList(imgs)
        print(positions)
        


else:
    print('user cancelled') 

