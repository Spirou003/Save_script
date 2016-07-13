# -*- coding: utf-8 -*-

"""
Todo:
- bug d'interruption de copie (os.stat(path).st_size et os.stat(filename).st_mtime)
- creer un depot github
"""

import shutil
import os
import traceback
import sys

import file

srcdir = file.getsrcdir()
dstdir = file.getdstdir()
ignore = file.getignore(srcdir)

errorfile = open("update_err.txt", "w+")

def print_error(string, filename):
    global errorfile
    print string+filename+"   "+str(sys.exc_info()[1])
    errorfile.write(string+filename+"   "+str(sys.exc_info()[1])+"\n")

def callback_ignore(dir, files):
    global ignore
    list = []
    for file in files:
        if (dir+os.sep+file in ignore):
            list.append(file)
    return list
#

file = open("out_new.txt", "r")
for filenames in file:
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
file.close()
file = open("out_modified.txt", "r")
for filenames in file:
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
file.close()
file = open("out_delete.txt", "r")
for filenames in file:
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
file.close()

errorfile.close()

