###Searches given directory for files containing (1) - (50) and deletes those files. (Windows) ###

import shutil
import os


def dedup(directory): #Accepts string in format "C:/users/downloads"
    files = os.listdir(directory)
    for file in files:
        for x in range(1,50): #Builds range for (1) - (50)
            x_str = str(x)
            dup = f"({x_str})"
            if dup in file: #searches files for match of duplicate strings
               srcfile = directory + "/" + file
               #print(srcfile) #uncomment this line to print matches files to console
							 
if __name__ == "__main__":
    dedup(directory)
