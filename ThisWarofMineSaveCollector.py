import sys
import os
import os.path
from os import path
import time
from datetime import datetime
from threading import Event
import shutil

exit = Event()

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def watchdir(profile):
    path_to_watch = os.path.abspath (".")
    path_to_watch = os.path.abspath ("C:\\Program Files (x86)\\Steam\\userdata\\"+profile+"\\282070\\remote")
    print ('watching: '+path_to_watch)
    now = datetime.now()
    dt_string = get_script_path()+"\\"+now.strftime("%d-%m-%Y_%H-%M-%S")
    os.mkdir(dt_string)
    print ('saving to: '+dt_string)
    try:
        if (path.exists(path_to_watch+"\\savedgames")) or (path.exists(path_to_watch+"\\storiessavedgames")):
            copysave(dt_string,path_to_watch)
        else:
            print ("Savegame not found!\n")
            usage()
            
    except Exception as e:
        print ('Error: ' + str(e))
        usage()


def copysave(dt_string,path_to_watch):
    f1 = os.path.getmtime(path_to_watch+"\\savedgames")
    f1alt = os.path.getmtime(path_to_watch+"\\savedgames.alt")
    f3 = os.path.getmtime(path_to_watch+"\\storiessavedgames")
    f3alt = os.path.getmtime(path_to_watch+"\\storiessavedgames.alt")
    count = 0
    while 1:
        time.sleep(5)
        f2 = os.path.getmtime(path_to_watch+"\\savedgames")
        f2alt = os.path.getmtime(path_to_watch+"\\savedgames.alt")
        f4 = os.path.getmtime(path_to_watch+"\\storiessavedgames")
        f4alt = os.path.getmtime(path_to_watch+"\\storiessavedgames.alt")
        if (f1 < f2) or (f1alt < f2alt):
            count = count+1
            print ("Save "+str(count)+' at '+datetime.fromtimestamp(f2).strftime("%d-%m-%Y_%H-%M-%S"))
            os.mkdir(dt_string+"\\"+"Save "+str(count))
            shutil.copy2 (path_to_watch+"\\savedgames",dt_string+"\\"+"Save "+str(count)+"\\savedgames")
            shutil.copy2 (path_to_watch+"\\savedgames.alt",dt_string+"\\"+"Save "+str(count)+"\\savedgames.alt")
            f1 = f2
            f1alt = f2alt
        if (f3 < f4) or (f3alt < f4alt):
            count = count+1
            print ("Save "+str(count)+' at '+datetime.fromtimestamp(f4).strftime("%d-%m-%Y_%H-%M-%S"))
            os.mkdir(dt_string+"\\"+"Save "+str(count))
            shutil.copy2 (path_to_watch+"\\storiessavedgames",dt_string+"\\"+"Save "+str(count)+"\\storiessavedgames")
            shutil.copy2 (path_to_watch+"\\storiessavedgames.alt",dt_string+"\\"+"Save "+str(count)+"\\storiessavedgames.alt")
            f3 = f4
            f3alt = f4alt
        

def usage():
    print ('usage: ThisWarofMineSaveCollector.py <steam account id>')
    sys.exit


def main(argv):

    watchdir(argv)
    sys.exit


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except Exception as e:
        print ('Error: ' + str(e))
        usage()
