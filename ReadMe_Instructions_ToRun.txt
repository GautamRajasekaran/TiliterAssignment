

#########Instrunctions to Run the scripts##############

1. PyScript_PlayVideo_Ex3_1.py

a.Edit the filepath to an absolute path to a video file
b.edit the videoHeight to an Int value
c.edit the videoWidth to an Int Value
d.edit the monocrome setting to True or False

######################################################

2.PyScript_ConverIntoMaskedVideo_Ex3_2.py

a.Edit the configurable settings , by commenting the other background subtractor and
uncomment the required extractor

b.Edit the InputFile path to an absolute path to a video file

c.Leave the OutputFile to create the _processed file under the same directory , if OutputFile
is filled to an absolute path to a video file then it will override.

######################################################


3.PyScript_PlayVideo_WithGUI_Ex4_1.py

a.Edit the filepath to an absolute path to a video file
b.edit the videoHeight to an Int value
c.edit the videoWidth to an Int Value
d.edit the monocrome setting to True or False

######################################################

4.DjangoWebApp_ConvertIntoMaskedVideo_Ex4_2

a.Cd to folder location
b.run in cmd prompt 'python manage.py runserver'
c.Navigate to 127.0.0.1:8000 in browser
d.Click on ProcessVideo button
e.Click on ChooseFile
f.Choose your desired file
g.Click on Process
h.Once processed , wait for the circling action on the browser.
g.File processed text should appear , click on the hyper link to the processed video file.
h.It should download the file to downloads folder.

######################################################

5.Digitdentification_Ex5_1

Final test accuracy = 90.8% 

a.Need to edit Digitdentification_Ex5_1\predict_Digit.py file to change EnvPath to local folder.
b.Can run predict_Digit.py to predict the image named ToPredict under Digitdentification_Ex5_1 folder
c.Before training , need to edit EnvPath in Digitdentification_Ex5_1\venv\TRAINER.py
c.Can run the training , the dataset used for training is in Digitdentification_Ex5_1\Dataset


######################################################

6.FlowerIdentification_Ex5_2

Final test accuracy = 82.5% 

a.Need to edit FlowerIdentification_Ex5_2\Predict_Flower.py file to change EnvPath to local folder.
b.Can run Predict_Flower.py to predict the image named ToPredict under FlowerIdentification_Ex5_2 folder
c.Before training , need to edit EnvPath in FlowerIdentification_Ex5_2\venv\TRAINER.py
c.Can run the training , the dataset used for training is in FlowerIdentification_Ex5_2\Dataset