import requests
import Spotify

import funcs
from pprint import pprint
import time
import  Osfuncs
import generate_config
import Leconfigs

generate_config.validaExistenciaConfig()



ACCESS_TOKEN = Leconfigs.clientID

#headers = requests.utils.default_headers()
#headers.update({
    #'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
#})

def main():
    current_track_id = None
    while True:
        current_track_info = Spotify.get_current_track(ACCESS_TOKEN)

        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )

            funcs.ResultadosBusca()

            nomeArtistaArrumado,nomeMusicaArrumado, nomeArtistaArrumadoBusca,nomeMusicaArrumadoBusca=funcs.Arrumador()

            #linkBusca = funcs.MontaUrlBusca(nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca)
            linktab = funcs.MontaLink_CC(nomeArtistaArrumado, nomeMusicaArrumado)
            print(linktab)
            current_track_id = current_track_info['id']

            Osfuncs.cls()
            tab,tabsemtags=funcs.PegaTab_CC(linktab)#cifraclubbase

            funcs.ValidaCapo_CC(linktab)

            print (tabsemtags)

            #linktab("https://www.cifraclub.com.br/badflower/ghost/")


    time.sleep(1)


if __name__ == '__main__':
    main()
