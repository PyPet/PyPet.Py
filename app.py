import os
clear = lambda: os.system('cls')
def actions(name):
    clear()
    print("\n \n \n")
    if(str(name).lower() == "sleep"):
        fileDogSleep = open("dogs/dogSleep.txt", "r")
        for line in fileDogSleep.readlines():
            print(line.replace('\n', ''))
        fileDogSleep.close()
    elif(str(name).lower() == "exit"):
        clear()
        exit()
    else:
        print("ERROR: El comando no es valido")

def onStart():
    clear()
    print("\n \n \n")
    fileDog1 = open("dogs/dog1.txt", "r")
    for line in fileDog1.readlines():
        print(line.replace('\n', ''))
    fileDog1.close()

    print("\n\n+-------------+\nLista de comandos: ")
    fileCmds = open("cmds.txt", "r")
    for line in fileCmds.readlines():
        print(line.replace('\n', ''))
    fileCmds.close()
    print("Que comando desea ejecutar: ")
    command = input()
    actions(command)
    print("\n\n+-------------+\nPulse enter para continuar")
    input()
    clear()
    onStart()

onStart()