import sentry_sdk
import os
import datetime
import time
import pygame
import yaml
import webbrowser
from threading import Thread
import threading
def clear(): lambda: cls


# Reporte Automatico de Errores de PTrue (RAE-PTrue)
sentry_sdk.init(
    "https://af4bd89b1244444a8039e7a881796ef4@o555373.ingest.sentry.io/5685102",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
fileYamlConfig = open("./config.yaml", "r")


def config(cname):
    configFile = yaml.load(open("./config.yaml", "r"))
    for key, value in configFile.items():
        if (key == cname):
            newconfig = yaml.load(str(value))
            return newconfig


alarms = {
    # "food1": "21:00",
    "food": "15:28",
    "power": "True"
}
def clear(): return os.system('cls')


def playdog(dogWAV):
    pygame.mixer.init()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    sound = pygame.mixer.Sound(os.path.join(dir_path, dogWAV))
    sound.play()


stopped = threading.Event()


def tfdt():
    while (not stopped):
        lcltime = datetime.datetime.now().strftime('%H:%M')
        if lcltime == alarms["food"]:
            playdog('alarms/dog1.wav')
            time.sleep(10)
        else:
            time.sleep(10)
        if (stopped.is_set()):
            break


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
    elif(str(name).lower() == "help"):
        fileCmds = open("cmds.txt", "r")
        for line in fileCmds.readlines():
            print(line.replace('\n', ''))
        fileCmds.close()
    elif(str(name).lower() == "eat"):
        def eatGetCode():
            printDog("dogEat")
            print("Que le vas a dar de comer? (Codigo de la tarjeta de Alimento)")
            toEat = input("Codigo > ").lower()
            noBreak = True
            for key, value in config("eatCodes").items():
                if (key == toEat and value == 'enabled'):
                    print("Pulsa ENTER para darle de comer")
                    input()
                    clear()
                    printDog("dogEat1")
                    playdog("alarms/dogEating.wav")
                    noBreak = False
            if (noBreak == True):
                eatGetCode()
        eatGetCode()
    elif(str(name).lower() == "config"):
        print("Configuracion \nActivar/Desactivar alarmas = alarms.<True/False>")
        opcinoncofig = input()
        if (str(opcinoncofig).lower().split(".")[0] == "alarms"):
            alarms["power"] = str(opcinoncofig).lower().split(".")[1]
    elif(str(name).lower() == "exit"):
        stopped.set()
        clear()
        exit()
    elif(str(name).lower() == "mm:calb"):
        print("Gameme es un programador :D")
        webbrowser.open(
            "https://www.youtube.com/channel/UC73IGChBfBr8zkuCXC9qjxA")
    elif(str(name).lower() == "mm:sin"):
        print('NO SLEEPING IN THE NETHER')
        webbrowser.open("https://www.youtube.com/watch?v=tF_0X6CKJd8")
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
