if (buscarSempre == "sim" or buscarSempre == "SIM" or buscarSempre == "Sim" or buscarSempre == "True"
        or buscarSempre == "TRUE" or buscarSempre == "true"):
    buscarSempreB = True
elif (
        buscarSempre == "nao" or buscarSempre == "NAO" or buscarSempre == "Nao" or buscarSempre == "não" or buscarSempre == "Não"
        or buscarSempre == "NÃO" or buscarSempre == "false" or buscarSempre == "FALSE" or buscarSempre == "False"):
    buscarSempreB = False
else:
    print("Buscar sempre invalido.")