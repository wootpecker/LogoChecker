import os

directory = "C:/Users/bener/Desktop/LogoChecker/LogoChecker/data/pdf"
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        with open(os.path.join(directory, filename)) as f:
            print(str(f))


from os import listdir
from os.path import isfile, join

mypath="data/pdf"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)