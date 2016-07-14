# -*- coding: utf-8 -*-

import shutil
import os
import sys

import file

def check(srcdir, dstdir):
    global N
    global sum
    global filedifftimes
    global ignore
    listnew = [] #nouveaux fichiers
    listdel = [] #supprimes
    listold = [] #modifies
    listerr = [] #non copiables
    srclist = os.listdir(srcdir)
    dstlist = os.listdir(dstdir)
    for srcfile in srclist:
        srcfilename = srcdir+os.sep+srcfile
        if (srcfilename in ignore):
            if (srcfile in dstlist):
                dstlist.remove(srcfile)
            continue
        if (srcfile in dstlist):
            if (os.path.isdir(srcfilename)):
                if (os.path.isdir(dstdir+os.sep+srcfile)):
                    res = check(srcfilename, dstdir+os.sep+srcfile)
                    listold.extend(res[0])
                    listnew.extend(res[1])
                    listdel.extend(res[2])
                    listerr.extend(res[3])
                else:
                    listerr.append(srcfilename)
            else:
                if (os.path.isdir(dstdir+os.sep+srcfile)):
                    listerr.append(srcfilename)
                else:
                    stold = os.stat(srcfilename)
                    stnew = os.stat(dstdir+os.sep+srcfile)
                    oold = stold.st_mtime
                    onew = stnew.st_mtime
                    sold = stold.st_size
                    snew = stnew.st_size
                    if (oold - onew > 0.5 or sold != snew):
                        listold.append(srcfilename)
            dstlist.remove(srcfile)
        else:
            listnew.append(srcfilename)
    for dstfile in dstlist:
        listdel.append(srcdir+os.sep+dstfile)
    return (listold, listnew, listdel, listerr)
#
srcdir = file.getsrcdir()
dstdir = file.getdstdir()
listdir = file.getlistdir()
ignore = file.getignore(srcdir)

print "   --- "+srcdir
print "   --- "+dstdir
print "   --- "+str(listdir)
print "   --- "+str(ignore)

listold = []
listnew = []
listdel = []
listerr = []
for dir in listdir:
    pathsrc = srcdir+os.sep+dir
    pathdst = dstdir+os.sep+dir
    if (os.path.isdir(pathsrc)):
        if (os.path.isdir(pathdst)):
            res = check(pathsrc, pathdst)
            listold.extend(res[0])
            listnew.extend(res[1])
            listdel.extend(res[2])
            listerr.extend(res[3])
        else:
            if (os.path.exists(pathdst)):
                listerr.append(pathsrc)
            else:
                listnew.append(pathsrc)
    else:
        listerr.append(pathsrc)
#
print "\n  Fichiers modifies:"
for el in listold:
    print "    "+el
print "\n  Fichiers crees:"
for el in listnew:
    print "    "+el
print "\n  Fichiers supprimes:"
for el in listdel:
    print "    "+el
print "\n  Fichiers erreur:"
for el in listerr:
    print "    "+el
out = open("out_modified.txt", "w+")
for el in listold:
    out.write(el+"\n")
out.close()
out = open("out_new.txt", "w+")
for el in listnew:
    out.write(el+"\n")
out.close()
out = open("out_delete.txt", "w+")
for el in listdel:
    out.write(el+"\n")
out.close()
out = open("out_err.txt", "w+")
for el in listerr:
    out.write(el+"\n")
out.close()
#




