This project contains pipleline for acoustic features extraction 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

--> For openSMILE Features

Download openSMILE from https://www.audeering.com/opensmile/


'OpenSmileFeatureExtraction.py' extract fetures from audio segments in 'INPUT_FOLDER' and saves the features in 'OUTPUT_FOLDER' in .arff files and write a CSV for all the audio segments 
in the same folder where 'OpenSmileFeatureExtraction.py' is located.

please mention your directories in 'paths.ini' configuration file

'INPUT_FOLDER' update this path with your audio segments folder (.wav files)

'OUTPUT_FOLDER' update this path with your output folder (.arff files)

'OPEM_SMILE' update this path with the location of openSMILE binary file i.e. SMILExtract

'FEATURE' update this path with the feature configuration file location in your machine such as for eGeMAPs the configuration file is 'eGeMAPSv01a.conf', and for interspeech 2013 computational paralinguistic challenege  'IS13_ComParE.conf'

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
