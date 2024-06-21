# Downdetector-status

# Requisitos
Python 3
requests
re


# Implementação 

cd /usr/lib/zabbix/externalscripts

Crie o arquivo downdetector.py

nano downdetector.py > cole o conteúdo de downdetector.py e salve 

python3 downdetector.py > espere finalizar 

ls > deve aparecer resultados.txt


chmod a+x resultados.txt 


# Configure o Cron pra rodar o downdetector.py

crontab -e      e cole        0,5,10,15,20,25,30,35,40,45,50,55 * * * * cd  /usr/lib/zabbix/externalscripts && python3 /usr/lib/zabbix/externalscripts/downdetector.py #downdetector

Vá até o frontend do zabbix e importe o host, edite a sua preferencia .


instagram
whatsapp
twitter
facebook
tiktok
banco-itau
nubank
caixa
banco-do-brasil
bradesco
sicoob
banco-pan
banco-inter
santander
picpay
bcb
nota-fiscal-eletronica
sefaz
youtube
google
gmail
globoplay
netflix
amazon-prime-instant-video
disney-plus
alelo
league-of-legends
league-of-legends-wild-rift
call-of-duty
free-fire
bet365
dataprev
receite-federal
fortnite
discord
hbo
Globo


