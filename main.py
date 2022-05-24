import logging

import generate_config
from os.path import exists

import Spotify
import funcs
from pprint import pprint
import time
import Osfuncs

import Leconfigs

# configExiste=generate_config.validaExistenciaConfig()
generate_config.validaExistenciaConfig()

ACCESS_TOKEN = Leconfigs.clientID
print(ACCESS_TOKEN)


def main():
    generate_config.validaExistenciaConfig()
    current_track_id = None
    while True:
        if Leconfigs.configValida == False:
            print("Configuracoes invalidas, verifique o  log para mais detalhes, encerrando")
            break
        current_track_info = Spotify.get_current_track(ACCESS_TOKEN)

        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )

            funcs.ResultadosBusca()

<<<<<<< Updated upstream
            nomeArtistaArrumado,nomeMusicaArrumado, nomeArtistaArrumadoBusca,nomeMusicaArrumadoBusca=funcs.Arrumador()

            #linkBusca = funcs.MontaUrlBusca(nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca)



            instrumento=Leconfigs.instrumento
            sitePreferencial=Leconfigs.sitePreferencial
            idEncaminhamento=0
            idEncaminhamento=funcs.CriaIdEncaminhamento(instrumento,sitePreferencial)
            buscarsempre=Leconfigs.buscarSempreB
            print (idEncaminhamento)

=======
            nomeArtistaArrumado, nomeMusicaArrumado, nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca = funcs.Arrumador()
>>>>>>> Stashed changes

            # linkBusca = funcs.MontaUrlBusca(nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca)

            instrumento = Leconfigs.instrumento
            sitePreferencial = Leconfigs.sitePreferencial
            idEncaminhamento = 0
            idEncaminhamento = funcs.CriaIdEncaminhamento(instrumento, sitePreferencial)
            buscarsempre = Leconfigs.buscarSempreB
            print(idEncaminhamento)

<<<<<<< Updated upstream


            #linktab = funcs.MontaLink_CC(nomeArtistaArrumado, nomeMusicaArrumado,idEncaminhamento)
            #print(linktab)
            

=======
            # linktab = funcs.MontaLink_CC(nomeArtistaArrumado, nomeMusicaArrumado,idEncaminhamento)
            # print(linktab)
>>>>>>> Stashed changes
            current_track_id = current_track_info['id']
            localizoutab_CC =funcs.localizoutab_CC
            Osfuncs.cls()
            print(buscarsempre)
            if (idEncaminhamento == 11 or idEncaminhamento == 12 or idEncaminhamento == 13 or idEncaminhamento == 14):
                # cc
                if buscarsempre:
                    funcs.CriaTermoBusca(idEncaminhamento)
                else:
                    linktab = funcs.MontaLink_CC(nomeArtistaArrumado, nomeMusicaArrumado, idEncaminhamento)
                    tab, tabsemtags = funcs.PegaTab_CC(linktab)  # cifraclubbase
                    funcs.ValidaCapo_CC(linktab)


                    print (tabsemtags)

            elif (idEncaminhamento == 21 or idEncaminhamento == 23 or idEncaminhamento == 24):
                funcs.CriaTermoBusca(idEncaminhamento)
            else:
                logging.error("Erro de id ")
                print("Erro de id ")

    time.sleep(1)


if __name__ == '__main__':
    main()
