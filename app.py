import os, datetime, time, pygame
from threading import Thread
alarms = {
    #"food1": "21:00",
    "food": "15:28",
    "power": "True"
}
clear = lambda: os.system('cls')
def playdog(dogWAV):
    pygame.mixer.init()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    sound = pygame.mixer.Sound(os.path.join(dir_path, dogWAV))
    sound.play()
def tfdt():
    while True:
        lcltime = datetime.datetime.now().strftime('%H:%M')
        if lcltime == alarms["food"]:
            playdog('alarms/dog1.wav')
            time.sleep(10)
            break
        else:
            time.sleep(10)
tfdtThread = Thread(target=tfdt)
def printDog(name):
    fileDog = open("dogs/"+name+".txt", "r")
    for line in fileDog.readlines():
        line2 = str(line.replace('\n', ''))
        print(line2)
    fileDog.close()
def actions(name):
    clear()
    print("\n \n \n")
    if(str(name).lower() == "sleep"):
        printDog("dogSleep")
        playdog("alarms/dogSleeping.wav")
    elif(str(name).lower()=="help"):
        fileCmds = open("cmds.txt", "r")
        for line in fileCmds.readlines():
            print(line.replace('\n', ''))
        fileCmds.close()
    elif(str(name).lower()=="eat"):
        printDog("dogEat")
        print("Pulsa ENTER para darle de comer")
        input()
        clear()
        printDog("dogEat1")
        playdog("alarms/dogEating.wav")
    elif(str(name).lower()=="config"):
        print("Configuracion \nActivar/Desactivar alarmas = alarms.<True/False>")
        opcinoncofig = input()
        if (str(opcinoncofig).lower().split(".")[0] == "alarms"):
            alarms["power"] = str(opcinoncofig).lower().split(".")[1]
    
    elif(str(name).lower() == "exit"):
        clear()
        print("Pulsa Ctrl + C y luego ENTER para cerrar")
        
    else:
        print("ERROR: El comando no es valido")



def onStart():
    clear()
    playdog("alarms/dog1.wav")
    print("\n \n \n")
    printDog("dog1")
    print("\n\n+-------------+\nEscribe 'help' para ver la lista de comandos: ")
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
    tfdtThread.start()
    onStart()
start()

