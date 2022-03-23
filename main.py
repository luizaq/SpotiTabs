import requests
import Spotify
from bs4 import BeautifulSoup
import funcs
from pprint import pprint
import time
import  Osfuncs
import generate_config
from googlesearch import search
generate_config.validaExistenciaConfig()

cavaco = False

ACCESS_TOKEN = 'BQDavckFZZTyKqV13ByHzL1Ea1yJreZGs8IdF1YUg2HikeIZ44CD86fYVppROmHVL6aP9FjjgK1Uh5Cmyg7NYOeY1GIRajBUZagwPIEZ-ITkTA-ZgV7u03zVUpNuhLyS_bu5KJPZKbILIfhQmhC4ZmNq'

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
#r = requests.get(url, headers=headers)
#soup = BeautifulSoup(r.text, 'html.parser')




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
            linktab = funcs.MontaLink(nomeArtistaArrumado, nomeMusicaArrumado)
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
