
import pandas as pd # Pandas para ler o arquivo csv
import os  
import time # Usado para aplicar um temporizador no processo do Selenium
import shutil as sh # Utilizado para mover arquivos localmente
import getpass as gp # Utilizado para extrair o nome do usuário logado no sistema  
from os import listdir # Utilizado na listagem de todos os arquivos na página de Downloads
from selenium import webdriver # Importando o Selenium para automatizar o processo de download do arquivo na página web




def extract_archive(cod):

    # Acessando o site do yahoo para fazer o download do arquivo .csv com os dados históricos do papel
    codigo = cod.upper() + '.SA'
    user = gp.getuser()
    
    try:
        navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        navegador.get(f'https://finance.yahoo.com/quote/{codigo}/history?p={codigo}')
        time.sleep(6)
    except:
        print('WebDriver ou Código da Ação Não encontrados')

    try:
        navegador.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()
        time.sleep(10)
    except:
        print('Elemento não encontrado')


    # Definindo o endereço local 
    download_pasta = f"/Users/{user}/Downloads"
    pasta_destino_csv = f"/Users/{user}/OneDrive - Programmer's Beyond IT/B3Project/Arquivos"
    pasta_origem_json = f"/Users/{user}/OneDrive - Programmer's Beyond IT/B3Project"
    pasta_destino_json = f"/Users/{user}/OneDrive - Programmer's Beyond IT/B3Project/JSON"

    csv = os.listdir(download_pasta)
    nome_csv = codigo + '.csv' 
    nome_json = codigo + ".json"

    resultado = nome_csv in csv 
    end_final = download_pasta + '/'
    

    if resultado == True:

        # Movendo da pasta Downloads para a pasta Arquivos 
        origem_csv = end_final + nome_csv
        destino_csv = pasta_destino_csv + '/' + nome_csv

        sh.move(origem_csv,destino_csv)

        # Transformando o CSV em JSON e movendo o arquivo transformado da pasta principal para a pasta JSON
        try:
            csv = pd.read_csv(destino_csv, sep=',')
            csv.to_json(nome_json, orient="records")
            print("Arquivo Convertido de CSV para JSON")

        except:
            print("Erro na transformação do arquivo")

        try:
            origem_json = pasta_origem_json + '/' + nome_json
            destino_json = pasta_destino_json + '/' + nome_json
            sh.move(origem_json,destino_json)
            print('Arquivo movido')

        except:
            print('Erro ao mover o arquivo')

    else:
        print('O Arquivo Não Existe, não movido')


    return print("Processo Finalizado")



extract_archive(input("Digite o código da ação: "))


