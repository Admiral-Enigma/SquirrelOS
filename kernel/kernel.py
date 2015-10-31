import sys, os
from glob import glob
commandList = ["help", "shutdown", "ls", "dir", "mkdir", "cd"]

def bootLoader():
    print("Welcome to SquirrelOS!")
    print("Made By Dem_Squirrel and FreakzDK \n")
    print("Type help to see the commands")
    commandLine()

def commandLine():
    cmd = input("> ")
    if cmd == commandList[0]:
        helpdist()
    if cmd == commandList[1]:
        shutdown()
    if cmd == commandList[2] or cmd == commandList[3]:
        showdir()
    if cmd.__contains__("mkdir"):
        dirName = cmd[5:]
        makedir(dirName)
    if cmd.__contains__("cd"):
        dirPath = cmd[2:]
        dirPath = dirPath.strip()
        changeDir(dirPath)

    for command in commandList:
        if cmd != commandList:
            print("This command wasn't found")
            commandLine()
        else:
            break
def helpdist():
    for cmd in commandList:
        print(cmd)
    commandLine()
def shutdown():
    sys.exit(0)

def showdir():
    getDir = os.getcwd()
    print(getDir)
    print(os.listdir(getDir))
    commandLine()

def makedir(name):
    os.makedirs("data/"+name)
    print("Made A dir"+name)
    commandLine()

def changeDir(path):
    os.chdir(os.getcwd()+"\\"+path)
    commandLine()

bootLoader()