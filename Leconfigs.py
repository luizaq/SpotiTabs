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


def ValidaInstrumento(instrumento):
    if (instrumento == "G" or instrumento == "g" or instrumento == "Guitar" or
            instrumento == "guitar" or instrumento == "GUITARRA" or instrumento == "guitarra"
            or instrumento == "v" or instrumento == "V" or instrumento == "GUITAR"):
        instrumento = "G"
        configValidaI = True

    elif (instrumento == "C" or instrumento == "c" or instrumento == "CAVACO"
          or instrumento == "cavaco" or instrumento == "cavaquinho" or instrumento == "CAVAQUINHO"
          or instrumento == "Cavaquinho" or instrumento == "Cavaco"):
        instrumento = "C"
        configValidaI = True

    elif (instrumento == "B" or instrumento == "b" or instrumento == "BASS" or instrumento == "bass"
          or instrumento == "Bass" or instrumento == "Baixo" or
          instrumento == "baixo" or instrumento == "BAIXO"):
        instrumento = "B"
    elif (instrumento == "U" or instrumento == "u" or instrumento == "Ukulele" or
          instrumento == "UKULELE" or instrumento == "ukulele"):
        instrumento = "U"
        configValidaI = True

    else:
        print("Instrumento escolhido invalido. Verifique o arquivo configurations.ini")
        #log
        configValidaI=False

    return instrumento,configValidaI


def ValidaSitePreferencial(sitePreferencial):
    if (sitePreferencial=="UG"or sitePreferencial=="ug"
            or sitePreferencial=="ULTIMATE GUITAR" or sitePreferencial=="ultimate guitar"
            or sitePreferencial=="Ultimate Guitar"):
        sitePreferencial="UG"
        configValidaT = True

    elif (sitePreferencial=="CC" or sitePreferencial=="cc" or
          sitePreferencial=="Cifra Clube"or sitePreferencial=="CIFRA CLUB"
          or sitePreferencial=="CIFRA CLUBE"):
        sitePreferencial = "CC"
        configValidaT=True
    else:
        print("Site preferencial invalido, verifique o arquivo configurations.ini")
        configValidaT= False
        #log
    return sitePreferencial,configValidaT

def ValidaCavaco(instrumento, sitePreferencial):
    if(sitePreferencial=="UG" and instrumento == "C"):
        print("Gringo nao conhece cavaco, selecione site primario cc no configurations.ini")
        configValidaT=False
        #log
    else:
        configValidaT=True
    return configValidaT

def ValidaToken(clientId):
    if (clientId == "xxx"):
        print("Token Invalido, e necessario adicionar seu token do spotify no arquivo configurations.ini")
        print("https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types=")
        # log
        configValidaT = False
    else:
        configValidaT=True

    return configValidaT

def ValidadorDeValidacoes(configValidaT,configValidaI,configValidaS,configValidaC):
    if (not configValidaT or not configValidaI or not configValidaS or not configValidaC):
        configValida=False
        #log
    else:
        print("Configs Validas")
        configValida = True
        #log
    return configValida



configs = read_config()
ignoraLetras = configs['TabSettings']["ignoraLetras"]
instrumento = configs['TabSettings']["instrumento"]
salvacifras = configs['TabSettings']["salvacifras"]
exibeConsole = configs['TabSettings']["exibeConsole"]
sitePreferencial = configs['TabSettings']["sitePreferencial"]
buscarSempre = configs['TabSettings']["buscarSempre"]

clientID = configs["Spotify"]["ClientId"]
clientSecret = configs["Spotify"]["ClientSecret"]

ignoraLetrasB, salvacifrasB, exibeConsoleB, buscarSempreB = converteBool(ignoraLetras, salvacifras, exibeConsole,


                                                                         buscarSempre)
configValidaT= ValidaToken(clientID)
instrumento,configValidaI=ValidaInstrumento(instrumento)
sitePreferencial,configValidaS=ValidaSitePreferencial(sitePreferencial)
configValidaC=ValidaCavaco(instrumento,sitePreferencial)



configValida=ValidadorDeValidacoes(configValidaT,configValidaI,configValidaS,configValidaC) #paratudo

print(ignoraLetras, instrumento, salvacifras, exibeConsole, sitePreferencial, buscarSempre)
print(ignoraLetrasB, instrumento, salvacifrasB, exibeConsoleB, sitePreferencial, buscarSempreB)
