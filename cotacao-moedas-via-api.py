from time import sleep
import requests
import os


while True:
    cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
    cotacoes_dic = cotacoes.json()

    print('Essa cotação é atualizada a cada 10 segundos')
    print('')
    print(f'Dolar: {cotacoes_dic["USD"]["bid"]}')
    print(f'Euro: {cotacoes_dic["EUR"]["bid"]}')
    print(f'BTC: {cotacoes_dic["BTC"]["bid"]}')
    sleep(10)
    os.system('cls')