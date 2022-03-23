import configparser


def imprimeConfig():
    read_file = open("configurations.ini", "r")
    content = read_file.read()
    print("Content of the config file are:\n")
    print(content)
    read_file.flush()
    read_file.close()


def read_config():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config


def converteBool(ignoraLetras, salvacifras, exibeConsole, buscarSempre):
    if (ignoraLetras == "sim" or ignoraLetras == "SIM" or ignoraLetras == "Sim" or ignoraLetras == "True"
            or ignoraLetras == "TRUE" or ignoraLetras == "true"):
        ignoraLetrasB = True
    elif (
            ignoraLetras == "nao" or ignoraLetras == "NAO" or ignoraLetras == "Nao" or ignoraLetras == "não" or ignoraLetras == "Não"
            or ignoraLetras == "NÃO" or ignoraLetras == "false" or ignoraLetras == "FALSE" or ignoraLetras == "False"):
        ignoraLetrasB = False
    else:
        print("Igonora letras invalido.")

    ###################salva cifras

    if (salvacifras == "sim" or salvacifras == "SIM" or salvacifras == "Sim" or salvacifras == "True"
            or salvacifras == "TRUE" or salvacifras == "true"):
        salvacifrasB = True
    elif (
            salvacifras == "nao" or salvacifras == "NAO" or salvacifras == "Nao" or salvacifras == "não" or salvacifras == "Não"
            or salvacifras == "NÃO" or salvacifras == "false" or salvacifras == "FALSE" or salvacifras == "False"):
        salvacifrasB = False
    else:
        print("salva cifras invalido.")

    ########################################exibe console
    if (exibeConsole == "sim" or exibeConsole == "SIM" or exibeConsole == "Sim" or exibeConsole == "True"
            or exibeConsole == "TRUE" or exibeConsole == "true"):
        exibeConsoleB = True
    elif (
            exibeConsole == "nao" or exibeConsole == "NAO" or exibeConsole == "Nao" or exibeConsole == "não" or exibeConsole == "Não"
            or exibeConsole == "NÃO" or exibeConsole == "false" or exibeConsole == "FALSE" or exibeConsole == "False"):
        exibeConsoleB = False
    else:
        print("Exibe console invalido.")

    ########################################## Buscar sempre

    if (buscarSempre == "sim" or buscarSempre == "SIM" or buscarSempre == "Sim" or buscarSempre == "True"
            or buscarSempre == "TRUE" or buscarSempre == "true"):
        buscarSempreB = True
    elif (
            buscarSempre == "nao" or buscarSempre == "NAO" or buscarSempre == "Nao" or buscarSempre == "não" or buscarSempre == "Não"
            or buscarSempre == "NÃO" or buscarSempre == "false" or buscarSempre == "FALSE" or buscarSempre == "False"):
        buscarSempreB = False
    else:
        print("Buscar sempre invalido.")

    return ignoraLetrasB, salvacifrasB, exibeConsoleB, buscarSempreB


configs = read_config()
ignoraLetras = configs['TabSettings']["ignoraLetras"]
instrumento = configs['TabSettings']["instrumento"]
salvacifras = configs['TabSettings']["salvacifras"]
exibeConsole = configs['TabSettings']["exibeConsole"]
sitePreferencial = configs['TabSettings']["sitePreferencial"]
buscarSempre = configs['TabSettings']["buscarSempre"]

ignoraLetrasB, salvacifrasB, exibeConsoleB, buscarSempreB = converteBool(ignoraLetras, salvacifras, exibeConsole,buscarSempre)
print(ignoraLetras, instrumento, salvacifras, exibeConsole, sitePreferencial, buscarSempre)
print(ignoraLetrasB, instrumento, salvacifrasB, exibeConsoleB, sitePreferencial, buscarSempreB)

