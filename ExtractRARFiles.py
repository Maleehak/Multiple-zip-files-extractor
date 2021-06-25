from os import listdir
from os.path import isfile, join
import zipfile
import os

def ZIPfilesName(path):
    if not type(path) is str:
        raise TypeError("Path of file must be string")
        
    files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".zip")]
    return files
    

def extractZIPFiles(files, targetDirectory):
    try:
        for file in files:
            file = targetDirectory + file
            with zipfile.ZipFile(file,"r") as zip_ref:
                directory = os.path.splitext(file)[0]
                print("Extracting "+ directory )
                zip_ref.extractall(directory)
                
        return "Successfully extracted all the files"
    except Exception as e:
        print(e)
        return e.message()
        
        
#directory = "E:/FYP/OOP Lab/Question2-B-Maliha/"
#files = ZIPfilesName(directory)
#extractZIPFiles(files, directory)