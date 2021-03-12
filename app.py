import os, datetime, time, pygame
from threading import Thread

clear = lambda: os.system('cls')
def printDog(name):
    fileDog = open("dogs/"+name+".txt", "r")
    for line in fileDog.readlines():
        print(line.replace('\n', ''))
    fileDog.close()
def actions(name):
    clear()
    print("\n \n \n")
    if(str(name).lower() == "sleep"):
        printDog("dogSleep")
    elif(str(name).lower()=="eat"):
        printDog("dogEat")
        print("Pulsa ENTER para darle de comer")
        input()
        clear()
        printDog("dogEat1")
    
    elif(str(name).lower() == "exit"):
        clear()
        exit()
    else:
        print("ERROR: El comando no es valido")
alarms = {
    "food": "21:00",
    #"food": "20:26",
    "status": True
}
def tfdt():
    while alarms["status"] == True:
        lcltime = datetime.datetime.now().strftime('%H:%M')
        if lcltime == alarms["food"]:
            pygame.mixer.init()
            dir_path = os.path.dirname(os.path.abspath(__file__))
            sound = pygame.mixer.Sound(os.path.join(dir_path, 'dog1.wav'))
            sound.play()
            break
        else:
            time.sleep(10)


def onStart():
    clear()
    print("\n \n \n")
    printDog("dog1")
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
def start():
    clear()
    printDog("title")
    print("\nPara abrir, pulsa ENTER")
    input()
    clear()
    Thread(target=tfdt).start()
    onStart()
start()

