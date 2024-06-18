import ssl
import re
import random
import requests
from bs4 import BeautifulSoup
import time
import cloudscraper

# Lista de URLs a serem verificadas
URLS = [
    "http://downdetector.com.br/fora-do-ar/instagram/",
    "http://downdetector.com.br/fora-do-ar/whatsapp/",
    "http://downdetector.com.br/fora-do-ar/twitter/",
    "http://downdetector.com.br/fora-do-ar/facebook/",
	"http://downdetector.com.br/fora-do-ar/tiktok/",
    "http://downdetector.com.br/fora-do-ar/banco-itau/",
    "http://downdetector.com.br/fora-do-ar/nubank/",
    "http://downdetector.com.br/fora-do-ar/caixa/",
    "http://downdetector.com.br/fora-do-ar/banco-do-brasil/",
    "http://downdetector.com.br/fora-do-ar/bradesco/",
    "http://downdetector.com.br/fora-do-ar/sicoob/",
    "http://downdetector.com.br/fora-do-ar/banco-pan/",
    "http://downdetector.com.br/fora-do-ar/banco-inter/",
    "http://downdetector.com.br/fora-do-ar/santander/",
    "http://downdetector.com.br/fora-do-ar/picpay/",
    "http://downdetector.com.br/fora-do-ar/bcb/",
    "http://downdetector.com.br/fora-do-ar/nota-fiscal-eletronica/",
	"http://downdetector.com.br/fora-do-ar/sefaz/",
	"http://downdetector.com.br/fora-do-ar/youtube/",
	"http://downdetector.com.br/fora-do-ar/google/",
	"http://downdetector.com.br/fora-do-ar/gmail/",
	"http://downdetector.com.br/fora-do-ar/globoplay/",
	"http://downdetector.com.br/fora-do-ar/netflix/",
	"http://downdetector.com.br/fora-do-ar/amazon-prime-instant-video/",
	"http://downdetector.com.br/fora-do-ar/disney-plus/",
	"http://downdetector.com.br/fora-do-ar/alelo/",
	"http://downdetector.com.br/fora-do-ar/league-of-legends/",
	"http://downdetector.com.br/fora-do-ar/league-of-legends-wild-rift/",
	"http://downdetector.com.br/fora-do-ar/call-of-duty/",
	"http://downdetector.com.br/fora-do-ar/free-fire/",
	"http://downdetector.com.br/fora-do-ar/bet365/",
	"http://downdetector.com.br/fora-do-ar/dataprev/",
	"http://downdetector.com.br/fora-do-ar/receite-federal/",
	"http://downdetector.com.br/fora-do-ar/fortnite/",
	"http://downdetector.com.br/fora-do-ar/discord/",
	"http://downdetector.com.br/fora-do-ar/hbo/"
]

# Lista de user agents
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

# Parâmetros de status
PARAMS = {
    'Relatórios de usuários indicam que não há problemas': 'success',
    'Relatórios de usuários indicam potenciais problemas': 'warning',
    'Relatórios de usuários indicam problemas': 'danger'
}



if ssl.OPENSSL_VERSION_INFO[0] < 1 or ssl.OPENSSL_VERSION_INFO[1] < 1 or ssl.OPENSSL_VERSION_INFO[2] < 1:
    craw = "requests"
else:
    craw = "cloudscraper"

# Função para fazer requisição com delay e tratamento de proxies
def request(url, proxies=None):
    headers = {'User-Agent': random.choice(user_agent_list)}
    if craw == "cloudscraper":
        scraper = cloudscraper.create_scraper()
        return scraper.get(url, headers=headers, proxies=proxies)
    else:
        return requests.get(url, headers=headers, proxies=proxies)

# Função para parsear o resultado do status
def parse_result(status_text):
    status_text = status_text.strip()
    if status_text == 'success':
        status_number = 1
    elif status_text == 'warning':
        status_number = 2
    elif status_text == 'danger':
        status_number = 3
    else:
        status_number = 0
    return status_number

# Função para checar o site
def check_site(url, proxies=None):
    response = request(url, proxies)
    if response is None or response.status_code != 200:
        return 0

    try:
        bs = BeautifulSoup(response.text, 'html.parser')
        dataParse = bs.find("div", {"class": "entry-title"})
        status = dataParse.text.strip()
        result = None
        if not status:
            raise ValueError('')
        for param in PARAMS:
            if re.compile(r"{}.*".format(param)).match(status):
                result = PARAMS[param]
        if not result:
            raise ValueError('')
        return parse_result(result)
    except Exception as err:
        failover = re.compile(".*status: '(.*)',.*", re.MULTILINE)
        failover_status = failover.findall(response.text).pop()
        return parse_result(failover_status)

if __name__ == '__main__':
    with open('resultados.txt', 'w') as file:
        for url in URLS:
            status_number = check_site(url)
            result_line = f"{url}Status:{status_number}\n"
            file.write(result_line)
            print(result_line)
            # Atraso aleatório entre 1 e 5 segundos entre as requisições
            time.sleep(random.uniform(1, 5))
