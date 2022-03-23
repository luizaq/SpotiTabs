from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# prepare the option for the chrome driver
#webdriver.Chrome('/Users/user_123/downloads/chrome_driver')
options = webdriver.Chrome(Options)
options.add_argument('headless')

# start chrome browser
browser = webdriver.Chrome(chrome_options=options)
browser.get("https://www.ultimate-guitar.com/search.php?search_type=title&value=beatles")
print(browser.current_url)
soup = BeautifulSoup(browser.page_source, 'lxml')
name_link = soup.find_all('a')
#name_link = soup.find_all('a', class_='_3DU-x JoRLr _3dYeW')
link = soup.find_all('href')
for n_link, l in zip(name_link,link):
    print(f'{n_link.text}\n{l.text}')
    print('---------')