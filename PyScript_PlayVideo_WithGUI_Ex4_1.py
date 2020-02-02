
import cv2
import imutils
import numpy as np
import tkinter
import image
import PIL.Image, PIL.ImageTk
from tkinter import Button

PrevFrames=[]
window = tkinter.Tk()

##################TO EDIT #####################################
FilePath=r'C:\Users\GautamVidhu\Documents\Coding\Python\TiliterAssignment\SupportingFiles\video_2.mp4'
VideoHeight=800
VideoWidth=800
Monocrome=True
FPS=120
##################TO EDIT #####################################




cap = cv2.VideoCapture(FilePath)

global Pausebuttonpressed
Pausebuttonpressed=False

global Backbuttonpressed
Backbuttonpressed=False

def showMsg():
    print('pause pressed')
    global Pausebuttonpressed
    Pausebuttonpressed=True


def showMsgBack():
    print('back pressed')
    global Backbuttonpressed
    Backbuttonpressed=True




if (cap.isOpened() == False):
    print("Error opening video stream or file")
b1 = Button(window, text='Pause',command=showMsg)
b1.pack(side=tkinter.BOTTOM, padx=5, pady=5)
b2 = Button(window, text='PrevFrame',command=showMsgBack)
b2.pack(side=tkinter.BOTTOM, padx=5, pady=5)


Var_FrameNumber=0
# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    Var_FrameNumber = Var_FrameNumber + 1

    if ret == True:
        frame = imutils.resize(frame, width=VideoWidth, height=VideoHeight)
        height, width, no_channels = frame.shape
        try:
            canvas
        except NameError:
            print("canvas gets defined")
            canvas = tkinter.Canvas(window, width=width, height=height)
            canvas.pack()
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if Monocrome:
            TkFrame = cv2.cvtColor(grayFrame, cv2.COLOR_BGR2RGB)
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(TkFrame))
            canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
        else:
            TkFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(TkFrame))
            canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)





        window.update()

        #window.mainloop()

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        PrevFrames.append(frame)
        key = cv2.waitKey(int(1000 / FPS))




        if Pausebuttonpressed is True:
            while True:
                window.update()
                if Backbuttonpressed is True:
                    Var_FrameNumber = Var_FrameNumber - 1
                    frame2 = imutils.resize(PrevFrames[Var_FrameNumber], width=VideoWidth, height=VideoHeight)
                    grayFrame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
                    if Monocrome:
                        TkFrame2 = cv2.cvtColor(grayFrame2, cv2.COLOR_BGR2RGB)
                        photo2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(TkFrame2))
                        canvas.create_image(0, 0, image=photo2, anchor=tkinter.NW)
                    else:
                        TkFrame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                        photo2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(TkFrame2))
                        canvas.create_image(0, 0, image=photo2, anchor=tkinter.NW)

                    window.update()
                    Backbuttonpressed=False



    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()