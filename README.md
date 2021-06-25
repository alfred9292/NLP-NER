# NLP-NER
Named Entitiy Recognition using spaCY

The analysis. py is used to detect errors that
1. made by spaCY only
2. made by Stanford NER only
3. made by both systems

In order to run it, please make sure you have put the file path of results file for spaCY and Stanford NER correctly.



The combiner 1. py is used to detect named entity inconsitency issue made by spaCY system, that means, when dividing the whole sentence, spaCY may not divide the sentence into the same fragemnt as the original test engb does.

in order to run it, please make sure you have put the correct file path for output.txt and outputlist.txt.

output.txt stores the original prediction made by trained spaCY model.


SpacyNER.py is the code to train the model. The code is based on spaCY training model on Github, I have added code to convert the input date to json format, and changed the number of iternation from 100 to 20  to save training time, also I have added lines to export the system prediction to the output file.
in order to run it, just make sure the you have put the correct file path for eng.train and eng.testb data for TRAIN-DATA and TEST-DATA.
