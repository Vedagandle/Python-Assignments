#Wap that copies all text files from one directory to other every 10 min
#accpt name of source and destination
#validate both
#copy only text files
#maintain log file of copied file
#avoid terminating if one file is not copies


import sys
import os
import schedule
import time

def CopyFiles(source, destination):   #source directory= from where we are copying txt file

    ret = os.path.exists(source)

    if ret == False:
        print("Source directory does not exist")
        return

    ret = os.path.isdir(source)

    if ret == False:
        print("Source is not a directory")
        return

    ret = os.path.exists(destination)    #destination directory=where we are pasting this txt files

    if ret == False:
        print("Destination directory does not exist")
        return

    ret = os.path.isdir(destination)

    if ret == False:
        print("Destination is not a directory")
        return

    logfile = open("Log.txt","a")

    for FolderName, SubFolderName, FileName in os.walk(source):

        for fname in FileName:

            if fname.endswith(".txt"):

                sourcefile = os.path.join(FolderName, fname)

                destinationfile = os.path.join(destination, fname)

                try:
                    fsource = open(sourcefile,"r")
                    fdestination = open(destinationfile,"w")

                    data = fsource.read()

                    fdestination.write(data)

                    fsource.close()
                    fdestination.close()

                    print(fname,"copied successfully")

                    logfile.write( " copied successfully"+fname +"\n")

                except:
                    print(fname,"cannot be copied")

                    logfile.write(" cannot be copied"+fname+"\n")

    logfile.close()


def main():

    if(len(sys.argv) != 3):
        print("Insufficient arguments")
        return

    namesource = sys.argv[1]
    namedestination = sys.argv[2]

    schedule.every(10).minutes.do(CopyFiles, namesource, namedestination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()