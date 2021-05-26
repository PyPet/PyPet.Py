import datetime  # Tiempo
import os  # Otros
import threading  # Importante - Procesos en segundo plano
import time  # Tiempo
import webbrowser  # Abrir sitios web
import pygame  # Sonido
import sentry_sdk  # RAE-PTrue
import yaml  # Config
def clear(): os.system("cls")  # Clear - Win: "cls" Linux/Mac: "clear"
# Imports de plugins
# ej: import <Plugin>

# Fin imports de plugins


# Reporte Automatico de Errores de PTrue (RAE-PTrue)
sentry_sdk.init(
    "https://af4bd89b1244444a8039e7a881796ef4@o555373.ingest.sentry.io/5685102",
    traces_sample_rate=1.0,
    environment="beta",
    release="beta@0.0.1"
)


class NotSqlCode():

    def read_config(self, cname, isList):
        configFile = yaml.load(open("./config.yaml", "r"))
        for key, value in configFile.items():
            if (key == cname):
                if (isList):
                    newconfig = yaml.load(str(value))
                    return newconfig
                else:
                    newconfig = str(value)
                    return newconfig

    alarms = {
        # "food1": "21:00",
        "food": "15:28",
        "power": "True"
    }

    def playdog(self, dogWAV):
        pygame.mixer.init()
        dir_path = os.path.dirname(os.path.abspath(__file__))
        sound = pygame.mixer.Sound(os.path.join(dir_path, dogWAV))
        sound.play()

    stopped = threading.Event()

    def alarm_system(self):
        while (not self.stopped):
            lcltime = datetime.datetime.now().strftime('%H:%M')
            if lcltime == self.alarms["food"]:
                self.playdog('alarms/dog1.wav')
                time.sleep(10)
            else:
                time.sleep(10)
            if (self.stopped.is_set()):
                break

    alarm_system_Thread = threading.Thread(target=alarm_system)

    def printDog(self, name):
        fileDog = open("dogs/"+name+".txt", "r")
        for line in fileDog.readlines():
            line2 = str(line.replace('\n', ''))
            print(line2)
        fileDog.close()

    def actions(self, name):
        clear()
        print("\n \n \n")
        if(str(name).lower() == "sleep"):
            self.printDog("dogSleep")
            self.playdog("alarms/dogSleeping.wav")
        elif(str(name).lower() == "help"):
            fileCmds = open("cmds.txt", "r")
            for line in fileCmds.readlines():
                print(line.replace('\n', ''))
            fileCmds.close()
        elif(str(name).lower() == "eat"):
            def eatGetCode():
                self.printDog("dogEat")
                print("Que le vas a dar de comer? (Codigo de la tarjeta de Alimento)")
                toEat = input("Codigo > ").lower()
                noBreak = True
                for key, value in self.read_config("eatCodes", True).items():
                    if (key == toEat and value == 'enabled'):
                        print("Pulsa ENTER para darle de comer")
                        input()
                        clear()
                        self.printDog("dogEat1")
                        self.playdog("alarms/dogEating.wav")
                        noBreak = False
                if (noBreak == True):
                    eatGetCode()
            eatGetCode()
        elif(str(name).lower() == "config"):
            print("Configuracion \nActivar/Desactivar alarmas = alarms.<True/False>")
            opcinoncofig = input()
            if (str(opcinoncofig).lower().split(".")[0] == "alarms"):
                self.alarms["power"] = str(opcinoncofig).lower().split(".")[1]
        elif(str(name).lower() == "exit"):
            self.stopped.set()
            clear()
            exit()
        # Dev Plugins
        elif(str(name).lower() == "mm:calb"):
            print("Gameme es un programador :D")
            webbrowser.open(
                "https://www.youtube.com/channel/UC73IGChBfBr8zkuCXC9qjxA")
        elif(str(name).lower() == "mm:sin"):
            print('YOU WONT CATCH ME SLEEPING IN THE NETHER')
            webbrowser.open("https://www.youtube.com/watch?v=tF_0X6CKJd8")
        # Fin Dev Plugins
        # Llamada de plugins

        # Fin llamada de plugins
        else:
            print("ERROR: El comando no es valido")

    def onStart(self):

        clear()
        self.playdog("alarms/dog1.wav")
        print("\n \n \n")
        self.printDog("dog1")
        print("\n\n+-------------+\nEscribe 'help' para ver la lista de comandos: ")
        print("Que comando desea ejecutar: ")
        command = input()
        self.actions(command)
        print("\n\n+-------------+\nPulse enter para continuar")
        input()
        clear()
        self.onStart()

    def start(self):

        clear()
        self.printDog("title")
        print("\nPara abrir, pulsa ENTER")
        input()
        clear()
        self.alarm_system_Thread.start()
        self.onStart()


NotSqlCode().start()
