# -*- coding: utf-8 -*-

"""
Todo:
- bug d'interruption de copie (os.stat(path).st_size et os.stat(filename).st_mtime)
"""

import shutil
import os
import traceback
import sys

import file

profilename = "default"
if (len(sys.argv) >= 2):
    profilename = sys.argv[1]
#

srcdir = file.getsrcdir(profilename)
dstdir = file.getdstdir(profilename)
ignore = file.getignore(profilename, srcdir)

errorfile = open(file.getprofiledir(profilename)+"update_err.txt", "w+")

def print_error(string, filename):
    global errorfile
    print string+filename+"   "+str(sys.exc_info()[1])
    errorfile.write(string+filename+"   "+str(sys.exc_info()[1])+"\n")
#
def callback_ignore(dir, files):
    global ignore
    list = []
    for file in files:
        if (dir+os.sep+file in ignore):
            list.append(file)
    return list
#

fnew = open(file.getprofiledir(profilename)+"out_new.txt", "r")
for filenames in fnew:
    filename = filenames.strip()
    if (filename in ignore):
        continue
    if (os.path.isdir(filename)):
        try:
            shutil.copytree(filename, filename.replace(srcdir, dstdir), ignore=callback_ignore)
        except Exception, e:
            print_error("dir : ", filename)
    else:
        try:
            shutil.copy(filename, filename.replace(srcdir, dstdir))
        except Exception, e:
            print_error("file: ", filename)
fnew.close()
fmod = open(file.getprofiledir(profilename)+"out_modified.txt", "r")
for filenames in fmod:
    filename = filenames.strip()
    if (filename in ignore):
        continue
    if (os.path.isdir(filename)): #ne devrait jamais arriver
        try:
            shutil.copytree(filename, filename.replace(srcdir, dstdir), ignore=callback_ignore)
        except Exception, e:
            print_error("dir : ", filename)
    else:
        try:
            shutil.copy(filename, filename.replace(srcdir, dstdir))
        except Exception, e:
            print_error("file: ", filename)
fmod.close()
fdel = open(file.getprofiledir(profilename)+"out_delete.txt", "r")
for filenames in fdel:
    filename = filenames.strip()
    if (os.path.isdir(filename.replace(srcdir, dstdir))):
        try:
            shutil.rmtree(filename.replace(srcdir, dstdir))
        except Exception, e:
            print_error("dir : ", filename)
    else:
        try:
            os.remove(filename.replace(srcdir, dstdir))
        except Exception, e:
            print_error("file: ", filename)
fdel.close()

errorfile.close()

