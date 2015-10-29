import sys, os
commandList = ["help", "shutdown", "ls", "dir"]

def bootLoader():
    print("Welcome to SquirrelOS!")
    print("Made By Dem_Squirrel and FreakzDK \n")
    print("Type help to see the commands")
    commandLine()

def commandLine():
    cmd = input("> ")
    if cmd == commandList[0]:
        helpList()
    if cmd == commandList[1]:
        shutDown()
    if cmd == commandList[2] or cmd == commandList[3]:
        showDir()

    for command in commandList:
        if cmd != commandList:
            print("This command wasn't found")
            commandLine()
        else:
            break

def helpList():
    for cmd in commandList:
        print(cmd)
    commandLine()
def shutDown():
    sys.exit(0)

def showDir():
    print(os.getcwd())

bootLoader()