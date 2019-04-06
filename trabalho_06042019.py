# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

#selenium funcionalidades
browser = webdriver.Firefox(executable_path="C:\selenium\geckodriver")
url = 'https://weather.com/pt-BR/clima/10dias/l/BRMG0645:1:BR'
browser.get(url)
time.sleep(2)

cidades = ['Bauru', 'Araraquara', 'Pederneiras']

for cidade in cidades:
    #pesquisar cidade
    field = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[8]/div[2]/div/div/div/div[1]/div/div[1]/div/input")
    field.send_keys(cidade + ", São Paulo, Brasil")
    time.sleep(1)
    botao = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[8]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/ul/li[1]")
    botao.click()
    time.sleep(3)
    
    #obter dados
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    table = soup.find('table', attrs={'class':'twc-table'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    
    #loop para obter dados da tabela
    print("CIDADE: "+cidade+"\n================================")
    
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]    
        info = [ele for ele in cols if ele]
        post = {
            "dia" : info[0],
            "descricao" : info[1],
            "min/max" : info[2],
            "precip" : info[3],
            "vento" : info[4],
            "umidade" : info[5]
        }
        print(post)
       
browser.close()
    