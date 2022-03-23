import requests
import Spotify
from bs4 import BeautifulSoup
from googlesearch import search

urlbase = "https://www.cifraclub.com.br"
headers = requests.utils.default_headers()
musicapossuicapo = False
localizoutab_CC = True
import Leconfigs

linkstemp = []
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

ACCESS_TOKEN = 'BQDavckFZZTyKqV13ByHzL1Ea1yJreZGs8IdF1YUg2HikeIZ44CD86fYVppROmHVL6aP9FjjgK1Uh5Cmyg7NYOeY1GIRajBUZagwPIEZ-ITkTA-ZgV7u03zVUpNuhLyS_bu5KJPZKbILIfhQmhC4ZmNq'

encontrou = True


def MontaLink(artista, musica):
    # ltt="/tuyo/sem-mentir/"
    ltt = "/" + artista + "/" + musica + "/"
    QtdLinksEncontrados = 0
    # /nome-artista/nome-musica
    # for link in linkstemp:
    # QtdLinksEncontrados+=1
    # busca os links na lista, link desejadk = ltt

    linkre = urlbase + ltt
    return linkre


def MontaTermoBuscaGoogle(artist, Nmusca):
    termobuscagoogle = artist + "+" + Nmusca
    return termobuscagoogle


def MontaTermoBusca_CC(artist, Nmusca):
    # https: // www.cifraclub.com.br /?q = zombie + -+Bad + Wolves
    urlbuscabase = "https://www.cifraclub.com.br/?q="
    urlparabusca = urlbuscabase + artist + "-" + Nmusca
    termobuscagoogle = artist + "+" + Nmusca
    return termobuscagoogle
    print(urlparabusca)


def PegaTab_CC(url):
    urlt = url
    r = requests.get(urlt, headers=headers)
    soupTab = BeautifulSoup(r.text, 'html.parser')
    # tab = soupTab.findAll('div', class_="cifra_cnt g-fix cifra-mono")
    tab = soupTab.findAll('pre')
    # soupTabSemtag=BeautifulSoup(markup, 'html.parser')

    file = open("tab.txt", "w")
    file.write("%s = %s\n" % ("tab", tab))
    file.close()

    tabsemtags = RemoveTagsTab_CC()
    return tab, tabsemtags


def RemoveTagsTab_CC():
    file = open("tab.txt", "r")
    Tabstring = file.read().replace('<b>', '').replace('</b>', ' ')

    if (Tabstring == "tab = []\n"):  # nao encontra tab.buscar no google?
        print("semtab")
        localizoutab_CC = False
        EncaminhaBusca()

    file.close()
    return Tabstring


def ValidaCapo_CC(url):
    urlt = url
    r = requests.get(urlt, headers=headers)
    soupCapo = BeautifulSoup(r.text, 'html.parser')
    capos = soupCapo.find('span', id="cifra_capo")
    capo = str(capos)
    capoold = capos

    caponova = capo.replace('<span>', '').replace('</span>', '').replace('<span data-cy="song-capo"', '').replace(
        'id="cifra_capo">', '').replace(' <a class="js-modal-trigger" title="alterar capotraste">', ' ').replace('</a>',
                                                                                                                 '')
    caponovat = ""
    caponovat = caponova
    caponova = caponova.replace('\n', '')
    caponova = caponova.replace('                            ', '=')

    # print(caponova)

    if (caponova == ' '):
        print("!sem capo!")
        musicapossuicapo = False
    elif ('=' in caponova):
        print("!!!!MUSICA TEM CAPO!!!!!")
        musicapossuicapo = True
        caponova = caponova.replace('=', '')
        print(caponova)
    else:
        print("Falha: nao sei se musica tem capo")
        ##salvar em log?
        musicapossuicapo = False

    return musicapossuicapo, caponova


def AjustaNomeArtistaBusca(artist):
    artisttemp = ''
    subs = '+'
    artisttemp = artist.replace(" ", "+")
    # print(artisttemp)
    return artisttemp


def AjustaNomeMusicaBusca(musica):
    musicatemp = ''
    subs = '+'
    musicatemp = musica.replace(" ", "+")
    # print(musicatemp)
    return musicatemp


def AjustaNomeArtista(artist):
    artisttemp = ''
    subs = '+'
    artisttemp = artist.replace(" ", "-")
    artisttemp = artisttemp.lower()
    # print(artisttemp)
    return artisttemp


def AjustaNomeMusica(musica):
    musicatemp = ''
    subs = '+'
    musicatemp = musica.replace(" ", "-")
    # print(musicatemp)
    musicatemp = musicatemp.lower()
    return musicatemp


def PegaNomeMusica(DicSpotify):
    nmusica = ''
    # {'id': '1eadPrzB2P0ikQcqhKSAtv', 'track_name': 'Zombie', 'artists': 'Bad Wolves', 'link': 'https://open.spotify.com/track/1eadPrzB2P0ikQcqhKSAtv'}
    print(DicSpotify)

    nmusica = DicSpotify['track_name']
    nmusicatemp = ''
    nmusicatemp += nmusica
    return nmusicatemp


def PegaNomeArtista(DicSpotify):
    nmusica = ''
    # {'id': '1eadPrzB2P0ikQcqhKSAtv', 'track_name': 'Zombie', 'artists': 'Bad Wolves', 'link': 'https://open.spotify.com/track/1eadPrzB2P0ikQcqhKSAtv'}
    print(DicSpotify)

    nartista = DicSpotify['artists']
    nartistatemp = ''
    nartistatemp += nartista
    return nartistatemp


def ValidaSelinkeLetra(link):
    # https://www.cifraclub.com.br/the-unlikely-candidates/novocaine/letra/
    if '/letra' in link:
        print('Link de letra')


def Arrumador():
    current_track_info = Spotify.get_current_track(ACCESS_TOKEN)
    nomeArtistaDesarrumado = PegaNomeArtista(current_track_info)
    nomeMusicaDesarrumado = PegaNomeMusica(current_track_info)

    nomeArtistaArrumado = AjustaNomeArtista(nomeArtistaDesarrumado)
    nomeMusicaArrumado = AjustaNomeMusica(nomeMusicaDesarrumado)
    nomeArtistaArrumadoBusca = AjustaNomeArtistaBusca(nomeArtistaDesarrumado)
    nomeMusicaArrumadoBusca = AjustaNomeMusicaBusca(nomeMusicaDesarrumado)

    return nomeArtistaArrumado, nomeMusicaArrumado, nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca


def ResultadosBusca():
    # gs-title
    # urlt = url
    urlt = "https://www.cifraclub.com.br/?q=zombie+-+Bad+Wolves#gsc.tab=0&gsc.q=zombie%20-%20Bad%20Wolves&gsc.page=1"
    r = requests.get(urlt, headers=headers)
    soupResultados = BeautifulSoup(r.text, 'html.parser')
    resultados = soupResultados.findAll('a', class_="gs-title")
    print(resultados)
    file = open("resultados.txt", "w")
    file.write("%s = %s\n" % ("res", resultados))
    file.close()


def PaginaArtista():
    soup = BeautifulSoup(r.text, 'html.parser')

    linksGeral = soup.find_all('a', class_="art_music-link")

    for a in soup.find_all('a', class_="art_music-link", href=True):
        i = 0
        print("Found the URL:", a['href'])
        linkstemp.append(a['href'])
        file = open("Python.txt", "w")
        file.write("%s = %s\n" % ("a", linksGeral))
        file.close()


def LeConfigs():
    f = open("config.txt", "r")
    lines = f.readlines()

    for line in lines:
        print(line, end="")


def EncaminhaBusca():
    nomeArtistaArrumado, nomeMusicaArrumado, nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca = Arrumador()

    sitePrimario = Leconfigs.sitePreferencial
    termobusca = MontaTermoBuscaGoogle(nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca)
    BuscaNoGoogle(sitePrimario, termobusca)


def BuscaNoGoogle(sitePrimario, termobusca):
    print("----------------------------------------------------------------------------")
    print("Cifra nao encontrada pelo metodo chute, mostrando resultados no google.....")
    print("----------------------------------------------------------------------------")


    if (sitePrimario == "UG"):
        query = "Ultimate Guitar" + termobusca + "tab"
        print("Seu site de busca primario e Ultimate guitar")
    elif (sitePrimario == "CC"):
        query = "CIFRA CLUB" + termobusca + "cifra"
        print("Seu site de busca primario e CifraCLub")
    else:
        print("ERRO SITE PRIMARIO INVALIDO")
        # Cifraclub usa google para obter buscas.##buscando pelo google pode ser utilziado tb o ug

    for j in search(query, tld="com", num=10, stop=10, pause=2):
        print(j)

# limpar o console entre musicas-ok
## lidar musica pausada
## validar outros instrumentos
## se nao encontra resultados, busca no google
# salvar a scifras
# abrir no browser
# seta site primario
# BuscaNoGoogle("CC", "ghost+badflower")
