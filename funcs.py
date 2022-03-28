import requests
import Spotify
from bs4 import BeautifulSoup
from googlesearch import search
import logging
from termcolor import colored

headers = requests.utils.default_headers()
musicapossuicapo = False
localizoutab_CC = True
import Leconfigs

ACCESS_TOKEN = Leconfigs.clientID
linkstemp = []
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

encontrou = True


def MontaLink_CC(artista, musica, idEncaminhamento):
    ltt = "/" + artista + "/" + musica + "/"
    base = "https://www.cifraclub.com.br"
    linkre = ""
    print("/""/""/""/""/""/""/""/""/")
    print(type(idEncaminhamento))
    if idEncaminhamento == 11:  # guitar
        linkre = base + ltt
        logging.info(linkre)
        print(linkre)
    elif idEncaminhamento == 12:  # cavaco
        linkre = base + ltt + "#tabs=false&instrument=cavaco"
        logging.info(linkre)
        print(linkre)

    elif idEncaminhamento == 13:  # baixo
        print("Chegou no if 13")
        linkre = base + ltt + "tabs-baixo/"
        print(linkre)
        logging.info(linkre)

    elif idEncaminhamento == 14:  # ukulele

        linkre = base + ltt + "#instrument=ukulele&tabs=false"
        logging.info(linkre)
        print(linkre)
    else:
        logging.error("erro ao identificar id de link e instrumento")

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
        logging.info("Cifra nao encontrada no CC")
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
        text = colored("MUSICA NAO POSSUI CAPO", 'red', attrs=['reverse', 'blink'])
        print(text)
        musicapossuicapo = False
        logging.info("MUSICA NAO POSSUI CAPO")
    elif ('=' in caponova):

        text = colored("!!!!MUSICA TEM CAPO!!!!!", 'green', attrs=['reverse', 'blink'])
        musicapossuicapo = True
        logging.info("Musica tem capo.")
        print(text)
        caponova = caponova.replace('=', '')
        print(caponova)
    else:

        musicapossuicapo = False
        logging.warning("Nao foi possivel validar se musica tem capo")

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
    artisttemp = artist.replace(" ", "-").replace("ã", "a").replace("ç", "c")
    artisttemp = artisttemp.lower()
    if (artisttemp == "exaltasamba"):
        artisttemp = "exaltasamba-musicas"
    # print(artisttemp)
    return artisttemp


def AjustaNomeMusica(musica):
    musicatemp = ''
    subs = '+'
    musicatemp = musica.replace(" ", "-").replace("ã", "a").replace("ç", "c")
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
    nomeArtistaArrumadoBusca = AjustaNomeArtistaBusca(nomeArtistaDesarrumado)

    if (nomeArtistaArrumadoBusca == "taylor+swift" or nomeArtistaArrumado == "taylor-swift" or nomeArtistaArrumado == "taylor-swift,-ed-sheeran"):
        nomeMusicaArrumado,nomeMusicaArrumadoBusca=RegraDaTaylor(nomeMusicaDesarrumado)

    else:
        nomeMusicaArrumado = AjustaNomeMusica(nomeMusicaDesarrumado)
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


def RegraDaTaylor(nomeMusicaDesarrumado):
    print("Caiu na regra da Taylor")
    logging.info("Caiu na regra da Taylor")
    print(nomeMusicaDesarrumado)

    nomeMusicaArrumado= nomeMusicaDesarrumado.replace(" (10 Minute Version) ","x")\
        .replace(" (Taylor's Version)","").replace("(Taylor's Version)","").replace(" (Acoustic Version)","")\
        .replace(" (From The Vault)","").replace(" (feat. Ed Sheeran) ","").replace(" ", "-")

    print(nomeMusicaArrumado)
    #nomeMusicaArrumado = nomeMusicaDesarrumado.replace(" ", "-")


    nomeMusicaArrumadoBusca = nomeMusicaDesarrumado.replace(" ", "+")

    nomeMusicaArrumadoT=nomeMusicaArrumado.lower()
    nomeMusicaArrumadoBuscaT = nomeMusicaArrumadoBusca.lower()



    return nomeMusicaArrumadoT,nomeMusicaArrumadoBuscaT

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


def ValidaInstrumento(instrumento, sitePreferencial):
    idEncaminhamento = 0
    # 1=cc,2=ug,3=songster, 4=??
    # 1=gutar,2=cavaco,3=baixo 4= uku ,5=??
    if (sitePreferencial == "CC"):

        if (instrumento == "G"):
            logging.info("ENCAMINHADO TAB =CHORDS,GUITAR,CC")
            idEncaminhamento = 11
            logging.info(idEncaminhamento)

        elif (instrumento == "C"):

            logging.info("ENCAMINHADO TAB =CHORDS,CAVACO,CC")
            idEncaminhamento = 12
            logging.info(idEncaminhamento)


        elif (instrumento == "B"):

            logging.info("ENCAMINHADO TAB =TAB,baixo,CC")
            idEncaminhamento = 13
            logging.info(idEncaminhamento)


        elif (instrumento == "U"):

            logging.info("INSTRUMENTO = UKULELE")
            idEncaminhamento = 14
            logging.info(idEncaminhamento)


        else:
            idEncaminhamento = 45
            logging.info(idEncaminhamento)
            logging.error("NAO ENCAMINHADO TAB = ????")

    return idEncaminhamento

# limpar o console entre musicas-ok
## lidar musica pausada
## validar outros instrumentos
## se nao encontra resultados, busca no google
# salvar a scifras
# abrir no browser
# seta site primario
# BuscaNoGoogle("CC", "ghost+badflower")
