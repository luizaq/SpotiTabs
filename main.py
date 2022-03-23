import requests
import Spotify
from bs4 import BeautifulSoup
import funcs
from pprint import pprint
import time
import os
from googlesearch import search

cavaco = False

ACCESS_TOKEN = 'BQBpUQKKcMoe7M_E17912SqXFOj_fIvq8cX3dSz6F1Yes1FV9MNJIckRQYyea7Ea1n8GKxQPKDI425GYXpiKnROitQRjF35WG3nBOSB6Nk0TuqwLkzSRdlzjTKsZVH5hwTTRTQUoKmhSL8Gkyw6DnBMz'
url = "https://www.cifraclub.com.br/tuyo/"

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')




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

            nomeArtistaDesarrumado = funcs.PegaNomeArtista(current_track_info)
            nomeMusicaDesarrumado = funcs.PegaNomeMusica(current_track_info)

            nomeArtistaArrumado = funcs.AjustaNomeArtista(nomeArtistaDesarrumado)
            nomeMusicaArrumado = funcs.AjustaNomeMusica(nomeMusicaDesarrumado)
            nomeArtistaArrumadoBusca = funcs.AjustaNomeArtistaBusca(nomeArtistaDesarrumado)
            nomeMusicaArrumadoBusca = funcs.AjustaNomeMusicaBusca(nomeMusicaDesarrumado)

            linkBusca = funcs.MontaUrlBusca(nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca)
            linktab = funcs.MontaLink(nomeArtistaArrumado, nomeMusicaArrumado)
            print(linktab)
            current_track_id = current_track_info['id']
            funcs.PegaTab(linktab)

    time.sleep(1)


if __name__ == '__main__':
    main()
