import shutil
import os
import time

def main():
    source ='C:\\Users\\Anna\\Desktop\\FolderA\\'
    destination ='C:\\Users\\Anna\\Desktop\\FolderB\\'  
    move_Files(source, destination)
    

def hours_since_mod(files):
    return (time.time() - os.path.getmtime(files))

def move_Files(source, destination):
    for files in os.listdir(source):
        filepath= source + files
        if hours_since_mod(filepath) < 86400:
            shutil.move(source + files,destination)
            print (destination + files)
        


if __name__ == "__main__":
    main()
