import requests
import Spotify
from bs4 import BeautifulSoup
from googlesearch import search
urlbase="https://www.cifraclub.com.br"
headers = requests.utils.default_headers()
linkstemp=[]
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
def MontaLink(artista,musica):
    #ltt="/tuyo/sem-mentir/"
    ltt= "/" + artista +"/" + musica+"/"
    QtdLinksEncontrados=0
# /nome-artista/nome-musica
    #for link in linkstemp:
        #QtdLinksEncontrados+=1
        #busca os links na lista, link desejadk = ltt

    linkre=urlbase+ltt
    return  linkre


def MontaUrlBusca(artist, Nmusca):
    # https: // www.cifraclub.com.br /?q = zombie + -+Bad + Wolves
    urlbuscabase = "https://www.cifraclub.com.br/?q="
    urlparabusca = urlbuscabase + artist + "-" + Nmusca
    print(urlparabusca)

def PegaTab(url):
    urlt=url
    r = requests.get(urlt, headers=headers)
    soupTab = BeautifulSoup(r.text, 'html.parser')
    tab = soupTab.findAll('div', class_="cifra_cnt g-fix cifra-mono")
    print(tab)
    file = open("tab.txt", "w")
    file.write("%s = %s\n" % ("tab", tab))
    file.close()
def AjustaNomeArtistaBusca(artist):
    artisttemp=''
    subs= '+'
    artisttemp=artist.replace(" ","+")
   # print(artisttemp)
    return artisttemp

def AjustaNomeMusicaBusca(musica):
    musicatemp=''
    subs= '+'
    musicatemp=musica.replace(" ","+")
    #print(musicatemp)
    return musicatemp

def AjustaNomeArtista(artist):
    artisttemp=''
    subs= '+'
    artisttemp=artist.replace(" ","-")
    artisttemp=artisttemp.lower()
   # print(artisttemp)
    return artisttemp

def AjustaNomeMusica(musica):
    musicatemp=''
    subs= '+'
    musicatemp=musica.replace(" ","-")
    #print(musicatemp)
    musicatemp=musicatemp.lower()
    return musicatemp

def PegaNomeMusica(DicSpotify):
    nmusica=''
#{'id': '1eadPrzB2P0ikQcqhKSAtv', 'track_name': 'Zombie', 'artists': 'Bad Wolves', 'link': 'https://open.spotify.com/track/1eadPrzB2P0ikQcqhKSAtv'}
    print(DicSpotify)

    nmusica =DicSpotify['track_name']
    nmusicatemp=''
    nmusicatemp+=nmusica
    return nmusicatemp
def PegaNomeArtista(DicSpotify):
    nmusica=''
#{'id': '1eadPrzB2P0ikQcqhKSAtv', 'track_name': 'Zombie', 'artists': 'Bad Wolves', 'link': 'https://open.spotify.com/track/1eadPrzB2P0ikQcqhKSAtv'}
    print(DicSpotify)

    nartista =DicSpotify['artists']
    nartistatemp=''
    nartistatemp+= nartista
    return nartistatemp
def ValidaSelinkeLetra(link):
#https://www.cifraclub.com.br/the-unlikely-candidates/novocaine/letra/
    if '/letra' in link:
        print('Link de letra')
def ResultadosBusca():
    #gs-title
    #urlt = url
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


def LeConfigs ():
    f = open("config.txt", "r")
    lines = f.readlines()

    for line in lines:
        print(line, end="")

def BuscaNoGoogle():
    # Cifraclub usa google para obter buscas.##buscando pelo google pode ser utilziado tb o ug
    print()
#limpar o console entre musicas
## lidar musica pausada
## validar outros instrumentos
## se nao encontra resultados, busca no google
# salvar a scifras