import os
import sys

prefixe = ""
if (len(sys.argv) >= 2 and "usetest" in sys.argv):
    prefixe = "test_"
#

def getsrcdir():
    file = open(prefixe+"srcdir.txt", "r")
    for line in file:
        return line.strip().replace("/", os.sep)
#
def getdstdir():
    file = open(prefixe+"dstdir.txt", "r")
    for line in file:
        return line.strip().replace("/", os.sep)
#
def getlistdir():
    file = open(prefixe+"list.txt", "r")
    listdir = []
    for line in file:
        listdir.append(line.strip().replace("/", os.sep))
    return listdir
#
def getignore(srcdir):
    file = open(prefixe+"ignore.txt", "r")
    listdir = []
    for line in file:
        listdir.append(srcdir+os.sep+(line.strip().replace("/", os.sep)))
    return listdir
#


