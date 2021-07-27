import os
import glob
import builtins
import re
from natsort import natsorted, ns
import configparser
config = configparser.ConfigParser()
config.read('paths.ini')
arffFolder=config['DEFAULT']['OUTPUT_FOLDER']

def main():

    	
    comb_arffFileName = "combinedARFF.csv" # please enter file name
    
    arff_files = [
        filename
        for filename
        in os.listdir(arffFolder)
        if filename.endswith('.arff')
        ]

    arff_files=natsorted(arff_files, alg=ns.IGNORECASE) 	
    combined_arffFile = open(comb_arffFileName,"w")
    headers_read= False
    for file in arff_files:
        print(file)
        arff_file = open(arffFolder + file,"r")
        if headers_read == False:
            for line in arff_file:
                #combined_arffFile.write(line)
                if line.find("liveturn_0")==1: # "unknown" for egemaps
                    print(file+','+line[10:-3])
                    combined_arffFile.write(file+','+line[10:-3]+'\n')
                if line.find("unknown")==1: # "unknown" for egemaps
                    print(file+','+line[10:-3])
                    combined_arffFile.write(file+','+line[10:-2]+'\n')
              #  print("header's file written\n")
              
            headers_read = True
        else:
            reached_data = False
            for line in arff_file:
                if line.strip() == "@data":
                    reached_data = True
                    continue
                if reached_data == True:
                    if line == "\n":
                        continue
                    combined_arffFile.write(file+','+line[10:-3]+'\n')
                    #print(file)
       #     print ("file appended\n")
    #print ("Combined file written\n")
            
    
                
if __name__ == '__main__':
   status = main()
    #sys.exit(status)
