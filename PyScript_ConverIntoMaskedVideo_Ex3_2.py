import cv2
import imutils
import numpy as np


##############CONFIGURE FOR DIFFERENT BACKGROUND EXTRACTION METHODS##################

#fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg= cv2.createBackgroundSubtractorMOG2(detectShadows = False)
#fgbg= cv2.createBackgroundSubtractorKNN()

##############CONFIGURE FOR DIFFERENT BACKGROUND EXTRACTION METHODS##################


####################TO BE EDITED#########################################
InputFilePath=r'C:\Users\GautamVidhu\Documents\Coding\Python\TiliterAssignment\SupportingFiles\video_1.mp4'
OutputFilePath=''
####################TO BE EDITED#########################################


if len(OutputFilePath)==0:
    OutputFilePath=InputFilePath.replace('.mp4','_processed.mp4')

cap = cv2.VideoCapture(InputFilePath)

TargetFPS=int(cap.get(cv2.CAP_PROP_FPS))
TargetHeight=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
TargetWidth=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OutputFilePath, fourcc, TargetFPS, (TargetWidth,TargetHeight))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret:

        fgmask = fgbg.apply(frame,0.005)

        for RowInd , PixelRow in enumerate(fgmask):
            for ColInd , PixelCol in enumerate(PixelRow):
                if PixelCol < 250:
                    frame[RowInd, ColInd, 0] = 0
                    frame[RowInd, ColInd, 1] = 0
                    frame[RowInd, ColInd, 2] = 0



        out.write(frame)          #Save it
        #cv2.imshow('Background Subtraction', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break                 #q to quit
    else:
        break                     #EOF                                          

cap.release()
out.release()
cv2.destroyAllWindows()