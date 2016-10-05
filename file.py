import os
import sys

def getprofiledir(profilename):
    return "profiles"+os.sep+profilename+os.sep

def profilefound(profilename):
    return (os.path.isdir("profiles"+os.sep+profilename) and \
    os.path.isfile("profiles"+os.sep+profilename+os.sep+"_dstdir.txt") and \
    os.path.isfile("profiles"+os.sep+profilename+os.sep+"_ignore.txt") and \
    os.path.isfile("profiles"+os.sep+profilename+os.sep+"_list.txt") and \
    os.path.isfile("profiles"+os.sep+profilename+os.sep+"_srcdir.txt"))

def getsrcdir(profilename):
    file = open(getprofiledir(profilename)+"_srcdir.txt", "r")
    srcdir = file.readline().strip().replace("/", os.sep)
    file.close()
    return srcdir
#
def getdstdir(profilename):
    file = open(getprofiledir(profilename)+"_dstdir.txt", "r")
    dstdir = file.readline().strip().replace("/", os.sep)
    file.close()
    return dstdir
#
def getlistdir(profilename):
    file = open(getprofiledir(profilename)+"_list.txt", "r")
    listdir = []
    for line in file:
        listdir.append(line.strip().replace("/", os.sep))
    file.close()
    return listdir
#
def getignore(profilename, srcdir):
    file = open(getprofiledir(profilename)+"_ignore.txt", "r")
    listdir = []
    for line in file:
        listdir.append(srcdir+os.sep+(line.strip().replace("/", os.sep)))
    file.close()
    return listdir
#


