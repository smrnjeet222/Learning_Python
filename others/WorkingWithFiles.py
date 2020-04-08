import os 
import shelve
import shutil 

os.chdir('C:\\Users\\simranjeet')

print(os.getcwd() ) #give current working directory 

print(os.path.join('C:\\', 'Users', 'Simranjeet'))

print(os.sep)

#IMP Walking a directory tree

for FolderName, SubFolder, FileName in os.walk('C:\\Users\\Simranjeet\\Desktop\\Python codes'):
    print ( 'the folder name is ' + FolderName)
    print ( 'the subfolder name is ' + str(SubFolder))
    print ( 'the file name is ' + str(FileName))
    print ()




