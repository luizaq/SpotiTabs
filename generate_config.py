import configparser
from os.path import exists
import Leconfigs
#https://www.codeproject.com/Articles/5319621/Configuration-Files-in-Python
# CREATE OBJECT

def validaExistenciaConfig():
    file_exists = exists("configurations.ini")
    if file_exists:
        print ("Arquivo existe")
        Leconfigs.read_config()
    elif not file_exists:
        print("Arquivo nao encontrado")
        criaConfigBase()

def criaConfigBase():
    config_file = configparser.ConfigParser()

    # ADD SECTION
    config_file.add_section("TabSettings")
    # ADD SETTINGS TO SECTION
    #secao, nome cofnig, valor config
    config_file.set("TabSettings", "ignoraLetras", "sim")
    config_file.set("TabSettings", "instrumento", "G") #Guitar,Cavavo,Baixo,Ukulele
    config_file.set("TabSettings", "salvacifras", "nao")
    config_file.set("TabSettings", "exibeConsole", "sim")
    config_file.set("TabSettings", "sitePreferencial", "CC")#UG OU CC
    config_file.set("TabSettings", "buscarSempre", "nao")# buscar sempre no google ou adivinhar link (somente cc)

    # SAVE CONFIG FILE
    with open(r"configurations.ini", 'w') as configfileObj:
        config_file.write(configfileObj)
        configfileObj.flush()
        configfileObj.close()

    print("Config file 'configurations.ini' created")

    # PRINT FILE CONTENT
    read_file = open("configurations.ini", "r")
    content = read_file.read()
    print("Content of the config file are:\n")
    print(content)
    read_file.flush()
    read_file.close()