import requests
import Spotify
from bs4 import BeautifulSoup
import funcs
import os
cavaco = False
linkstemp=[]
urlbase="https://www.cifraclub.com.br"
linkrealoficial= ""
ACCESS_TOKEN = 'BQAZjgWWsQg6rs2bp4G_6baHqkFS-m5iBBks799pyTP3BpNt7BWogBUNZMiEjXVQZ1FsEaNBLtNJh-22-nQrVwyqq9dpo0arfP8hiZpVxIwF3Obkvd9XRzGs7nZu9JO4Mj-avPplV3AmFUb73ITsXViv'
testedic= {'id': '1eadPrzB2P0ikQcqhKSAtv', 'track_name': 'Zombie', 'artists': 'Bad Wolves', 'link': 'https://open.spotify.com/track/1eadPrzB2P0ikQcqhKSAtv'}
def MontaLink(artista,musica):
    ltt="/tuyo/sem-mentir/"
    ltt= "/" + artista +"/" + musica
    QtdLinksEncontrados=0
# /nome-artista/nome-musica
    for link in linkstemp:
        QtdLinksEncontrados+=1
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
   # print(artisttemp)
    return artisttemp

def AjustaNomeMusica(musica):
    musicatemp=''
    subs= '+'
    musicatemp=musica.replace(" ","-")
    #print(musicatemp)
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



#url = "https://www.ultimate-guitar.com/search.php?search_type=title&value=beatles"
#url = "https://www.reddit.com/r/learnpython/wiki/index"
url = "https://www.cifraclub.com.br/tuyo/"

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
urlc='https://www.cifraclub.com.br/taylor-swift/all-too-well-10-minute-version/'
r = requests.get(url, headers= headers)
r2 = requests.get(urlc, headers= headers)

#get url
#r= requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


linksGeral = soup.find_all('a',class_= "art_music-link")

for a in soup.find_all('a',class_= "art_music-link",href= True):
    i=0
    print( "Found the URL:", a['href'])
    linkstemp.append(a['href'])



current_track_info = Spotify.get_current_track(ACCESS_TOKEN)
ResultadosBusca()
AjustaNomeArtista("Bad Wolf")
#print(current_track_info)


#urlt = url
#print (linkstemp)
#print(linkstemp.len())

#tab= soup.findAll('div',class_="cifra_cnt g-fix cifra-mono")


nomeMusicaDesarrumado=funcs.PegaNomeMusica(current_track_info)
nomeArtistaDesarrumado=funcs.PegaNomeArtista(current_track_info)
nomeArtistaArrumado=funcs.AjustaNomeArtista(nomeArtistaDesarrumado)
nomeMusicaArrumado=funcs.AjustaNomeMusica(nomeMusicaDesarrumado)


nomeArtistaArrumadoBusca=funcs.AjustaNomeArtistaBusca(nomeArtistaDesarrumado)
nomeMusicaArrumadoBusca=funcs.AjustaNomeMusicaBusca(nomeMusicaDesarrumado)

print(nomeArtistaArrumado)
print(nomeMusicaArrumado)

linkBusca = funcs.MontaUrlBusca(nomeArtistaArrumadoBusca,nomeMusicaArrumadoBusca)
linktab=funcs.MontaLink(nomeArtistaArrumado,nomeMusicaArrumado)
print(linktab)

PegaTab(linktab)
#linkrealoficial= MontaLink()
#print(linkrealoficial)
#links = soup.find_all('a',class_= "art_music-link")


#print (links)
#NomeMusica= ('Vidaloca')
#ind= links.index(NomeMusica)
#print (ind)

file = open("Python.txt", "w")
file.write("%s = %s\n" % ("a", linksGeral))

file.close()
#print(links[1])
#print(links)
#for a in soup.find_all("a"):
    #print("Found the URL:", a['href'])
#ltemp = links[1]

#ltempind= ltemp.find("=")
#print(type(ltemp))
#print(ltempind)
#print (ltemp)




