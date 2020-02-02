
import cv2
import imutils
import numpy as np

PrevFrames=[]

###################TO BE EDITED########################
FilePath=r'C:\Users\GautamVidhu\Documents\Coding\Python\TiliterAssignment\SupportingFiles\video_1.mp4'
VideoHeight=800
VideoWidth=800
Monocrome=False
FPS=120
###################TO BE EDITED########################


cap = cv2.VideoCapture(FilePath)




if (cap.isOpened() == False):
    print("Error opening video stream or file")

Var_FrameNumber=0
# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    Var_FrameNumber = Var_FrameNumber + 1
    if ret == True:
        frame = imutils.resize(frame, width=VideoWidth, height=VideoHeight)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        PrevFrames.append(frame)
        key = cv2.waitKey(int(1000 / FPS))
        if Monocrome:
            cv2.imshow('Frame', grayFrame)
        else:
            cv2.imshow('Frame', frame)

        # Press q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        # Press p on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('p'):
            while True:
                if cv2.waitKey(25) & 0xFF == ord('b'):
                    Var_FrameNumber = Var_FrameNumber - 1
                    frame2 = imutils.resize(PrevFrames[Var_FrameNumber], width=VideoWidth, height=VideoHeight)
                    grayFrame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
                    if Monocrome:
                        cv2.imshow('Frame', grayFrame2)
                    else:
                        cv2.imshow('Frame', frame2)



    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()