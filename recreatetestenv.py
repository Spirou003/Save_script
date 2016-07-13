import shutil
import os
import sys

def recover(dir):
    if (os.path.exists(dir)):
        if (os.path.isdir(dir)):
            shutil.rmtree(dir)
        else:
            os.remove(dir)
    shutil.copytree(dir+" - Copie", dir)
#
recover("new")
recover("old")

if (len(sys.argv) >= 2):
    file = open("old/dir/dir3/long_fichier.txt", "w+")
    i = 0
    while (i < 150000000):
        file.write(str(i)+"\n")
        i += 1
    #
    file.close()
#