
import requests
import Spotify
from bs4 import BeautifulSoup
from googlesearch import search



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


def MontaLink_CC(artista, musica):
    # ltt="/tuyo/sem-mentir/"
    ltt = "/" + artista + "/" + musica + "/"

    base = "https://www.cifraclub.com.br"
    linkre = ""
    print("/""/""/""/""/""/""/""/""/")
    #print(type(idEncaminhamento))
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

    
    # /nome-artista/nome-musica
    # for link in linkstemp:
    # QtdLinksEncontrados+=1
    # busca os links na lista, link desejadk = ltt


    linkre = "https://www.cifraclub.com.br" + ltt
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


    if (Tabstring == "tab = []\n"):  # nao encontra tab.buscar no google
        logging.info("Cifra nao encontrada no CC")
<<<<<<< Updated upstream
        Print("Cifra nao encontrada no CC")

=======
        print("Cifra nao encontrada no CC")
>>>>>>> Stashed changes
        localizoutab_CC = False
    ###ajustar para buscarcom o id correto.
        CriaTermoBusca(11)

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


def CriaTermoBusca(idEncaminhamento):
    nomeArtistaArrumado, nomeMusicaArrumado, nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca = Arrumador()
    idE=idEncaminhamento
    sitePrimario = Leconfigs.sitePreferencial
    termobusca = MontaTermoBuscaGoogle(nomeArtistaArrumadoBusca, nomeMusicaArrumadoBusca)
    #BuscaNoGoogle(termobusca)
    EncaminhaBusca(idE,termobusca)

def EncaminhaBusca(idEncaminhamento,termobusca):

    if (idEncaminhamento == 11):
        query= "CIFRA CLUB" + "+" +termobusca + "+" + "cifra"
    elif  (idEncaminhamento == 12):
        query = "CIFRA CLUB" + "+" + termobusca + "+" +"cifra" + "+" + "cavaco"

    elif (idEncaminhamento == 13):

        query = "CIFRA CLUB" + "+" +termobusca + "+" + "cifra" + "+" + "baixo"

    elif (idEncaminhamento == 14):

        query = "CIFRA CLUB" + "+" + termobusca + "+" + "cifra" + "+" + "ukulele"

    elif (idEncaminhamento ==21):
        query = "Ultimate Guitar" + "+" + termobusca + "+" + "tab"

    elif (idEncaminhamento == 23):
        query = "Ultimate Guitar" + "+" + termobusca + "+" + "tab" + "+" + "bass"

    elif (idEncaminhamento==24):
        query = "Ultimate Guitar" + "+" + termobusca + "+" + "tab" + "+" + "ukulele"

    BuscaNoGoogle(query)

def BuscaNoGoogle(query):
    print("----------------------------------------------------------------------------")
    print("Mostrando resultados no google.....")
    print("----------------------------------------------------------------------------")
    print (query)


    for j in search(query, tld="com", num=10, stop=10, pause=2):
        print(j)



def CriaIdEncaminhamento(instrumento, sitePreferencial):
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

            logging.info("INSTRUMENTO = UKULELE,CHORD , CC")
            idEncaminhamento = 14
            logging.info(idEncaminhamento)




    elif (sitePreferencial == "UG"):

        if (instrumento == "G"):
            logging.info("ENCAMINHADO TAB =CHORDS,GUITAR,UG")
            idEncaminhamento = 21
            logging.info(idEncaminhamento)

        elif (instrumento == "C"):

            logging.info("ENCAMINHADO TAB =CHORDS,CAVACO,UG")
            idEncaminhamento = 22
            logging.info(idEncaminhamento)
            logging.error("Gringo nao toca cavaco")

        elif (instrumento == "B"):

            logging.info("ENCAMINHADO TAB =TAB,baixo,UG")
            idEncaminhamento = 23
            logging.info(idEncaminhamento)

        elif (instrumento == "U"):

            logging.info("INSTRUMENTO = UKULELE, CHORDS ,UG")
            idEncaminhamento = 24
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
