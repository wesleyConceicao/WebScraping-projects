"""
A IDEIA É QUE ELE IDENTIFIQUE O NUMERO DE INGRESSOS E STORES DISPONIVEIS E ENVIE PARA O USUARIO
QUEM SABE FUTURAMENTE COLOCAR O BOT PARA COMPRA OS INGRESSOS AUTOMATICAMENTE COM A INTERFACE COM NUMERO DE USUARIOS
QUE QUEREM OS INGRESSO E OS SETORES.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from anticaptchaofficial.recaptchav2proxyless import *
import urllib
import chromedriver_binary
import random
import time
import pandas as pd
from bs4 import BeautifulSoup
import random
import rapidfuzz
import undetected_chromedriver as uc
import pandas as pd
import pytesseract
from PrettyColorPrinter import add_printer
import numpy as np


""" BAIXAR A VERSÃO MAIS ATUAL DO CRHOME DRIVER """

# from auto_download_undetected_chromedriver import download_undetected_chromedriver

# folder_path = "c:\\download2thisfolder20"
# chromedriver_path = download_undetected_chromedriver(
#     folder_path, undetected=True, arm=False, force_update=True
# )
# import undetected_chromedriver as uc

# driver = uc.Chrome(
#     driver_executable_path=chromedriver_path, headless=False, use_subprocess=True
# )

"""
COLOCAR O PERFIL DO USUARIO E OS COOKIES PARA BURLAR QUALQUER POSSIBILIDADE DE IMPEDIMENTO E INDENTIFICAÇÃO DO BOT 
PODEM SER DUAS OPÇÕES.

1° - ASSIM QUE O USUARIO LOGAR A PRIMEIRA VEZ ARMAZENAR OS COOKIES E ASSIM IR REPETINDO 
2° - LOGAR DIRETO COM PERFIL GOOGLE DO USUARIO E SEMPRE USAR ELE E IR SALVANDO OS COOKIES COMO SE FOSSE UM PSEUDO USUARIO 
ARMAZENANDO OS DADOS PARA NÃO TER PROBLEMA DE SER PEGO.   
 
"""

service = Service(executable_path="./chromedriver.exe")
options = webdriver.ChromeOptions()

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome(service=service, options=options)

#'https://flamengo.superingresso.com.br/#!/home'
wd.get('https://flamengo.superingresso.com.br/#!/home') # colocar aqui site do flamengo
wd.implicitly_wait(10)

#CLICA PARA ENTRAR NO EMAIL
wd.find_element(By.XPATH, '/html/body/div[2]/div/header/div/nav/span/a[2]/span').click()
time.sleep(5)

#CLICO PARA FALAR QUE NÃO SOU SÓCIO
wd.find_element("xpath",'//*[@id="dialogContent_0"]/md-card/div/div/a[2]/div').click()
time.sleep(5)

#INSIRO O EMAIL
email = wd.find_element(By.NAME, "_username") #loginKey
email.send_keys("wesley.cconcei@gmail.com")
time.sleep(5)

#INSIRO A SENHA
senha = wd.find_element(By.NAME,"_password") #.send_keys("@94256903Wl")
senha.send_keys("@9425_6903Wl")
time.sleep(5)

# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import whisper
import warnings
warnings.filterwarnings("ignore")

model = whisper.load_model("base")

def transcribe(url):
    with open('.temp', 'wb') as f:
        f.write(requests.get(url).content)
    result = model.transcribe('.temp')
    return result["text"].strip()

def click_checkbox(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver.find_element(By.ID, "recaptcha-anchor-label").click()
    driver.switch_to.default_content()

def request_audio_version(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    driver.find_element(By.ID, "recaptcha-audio-button").click()

def solve_audio_captcha(driver):
    text = transcribe(driver.find_element(By.ID, "audio-source").get_attribute('src'))
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
  
    driver.get("https://www.google.com/recaptcha/api2/demo")
    click_checkbox(driver)
    time.sleep(1)
    request_audio_version(driver)
    time.sleep(1)
    solve_audio_captcha(driver)
    time.sleep(10)

# PASSO PELO RECAPTCHA
add_printer(1)
import mousekey

mkey = mousekey.MouseKey()
mkey.enable_failsafekill("ctrl+e")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from fast_ctypes_screenshots import (
    ScreenshotOfOneMonitor,
)


def get_screenshot_tesser(minlen=2):
    with ScreenshotOfOneMonitor(
        monitor=0, ascontiguousarray=True
    ) as screenshots_monitor:
        img5 = screenshots_monitor.screenshot_one_monitor()
    df = pytesseract.image_to_data(img5, output_type="data.frame")
    df = df.dropna(subset="text")
    df = df.loc[df.text.str.len() > minlen].reset_index(drop=True)
    return df


def move_mouse(
    x,
    y,
    variationx=(-5, 5),
    variationy=(-5, 5),
    up_down=(0.2, 0.3),
    min_variation=-10,
    max_variation=10,
    use_every=4,
    sleeptime=(0.009, 0.019),
    linear=90,
):
    mkey.left_click_xy_natural(
        int(x) - random.randint(*variationx),
        int(y) - random.randint(*variationy),
        delay=random.uniform(*up_down),
        min_variation=min_variation,
        max_variation=max_variation,
        use_every=use_every,
        sleeptime=sleeptime,
        print_coords=True,
        percent=linear,
    )


if __name__ == "__main__":
    options = uc.ChromeOptions()
    userdir = "c:\\chromeprofiletest"
    options.add_argument(f"--user-data-dir={userdir}")
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    driver.get(r"https://jurisprudencia.trt15.jus.br/")
    sleep(20)
    df = get_screenshot_tesser(minlen=2)
    df = pd.concat(
        [
            df,
            pd.DataFrame(
                rapidfuzz.process_cpp.cdist(["Imnot", "arobot"], df.text.to_list())
            ).T.rename(columns={0: "imnot", 1: "arobot"}),
        ],
        axis=1,
    )

    try:
        vamosclicar = (
            np.diff(
                df.loc[
                    ((df.imnot == df.imnot.max()) & (df.imnot > 90))
                    | ((df.arobot == df.arobot.max()) & (df.arobot > 90))
                ][:2].index
            )[0]
            == 1
        )
    except Exception:
        vamosclicar = False

    if vamosclicar:
        x, y = df.loc[df.imnot == df.imnot.max()][["left", "top"]].__array__()[0]
        move_mouse(
            x,
            y,
            variationx=(-10, 10),
            variationy=(-10, 10),
            up_down=(0.2, 0.3),
            min_variation=-10,
            max_variation=10,
            use_every=4,
            sleeptime=(0.009, 0.019),
            linear=90,
        )

#CLICK DE ENVIAR O EMAIL
wd.find_element(By.XPATH, '//*[@id="dialogContent_3"]/md-card[2]/div/div[2]/form/div[2]/button/span').click()
time.sleep(5)

""" VAI CHECAR SE TEM INGRESSO DISPONIVEL
CASO TENHA INGRESSO DESPONIVEL ELE VAI AVISAR VIA WHATSAPP """

def checkForStock(url):
 # soup = BeautifulSoup(wd.page_source)
 wd.get(url)
 soup = BeautifulSoup(wd.page_source, features="html.parser")
 items = soup.find("div", {"class": "items-grid-view"})

 items_processed = []

 for row in items.findAll("div", {"class": "item-cell"}):
  row_processed = []
  itemTitle = row.find("a", {"class": "item-title"})
  itemPromoText = row.find("p", {"class": "item-promo"})
  itemPrice = row.find("li", {"class": "price-current"})

  status = "Available"

  if itemPromoText and itemPromoText.text == "OUT OF STOCK":
   status = "Sold Out"

  if itemTitle:
   row_processed.append(itemTitle.text)
   row_processed.append(itemPrice.find("strong").text)
   row_processed.append(itemTitle.get("href"))
   row_processed.append(status)

  if row_processed:
   items_processed.append(row_processed)
 # cells[3].find("img"valid)["src"]
 # columns = ["ImageUrl","Origin"]

 df = pd.DataFrame.from_records(items_processed, columns=["Item Title", "Item Price", "URL", "Status"])

 df["Item Price"] = df["Item Price"].apply(lambda x: x.replace(",", ""))
 df["Item Price"] = pd.to_numeric(df["Item Price"])

 return df

#CASO TENHA INGRESSO DISPONIVEL ELE VAI ENVIAR VIAR WHATSAPP

"""
AVISO O USUARIO O NUMERO DE INGRESSOS DISPONIVEIS E OS SETORES DISPONIVEIS 
"""
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

# Ler planilha e guardar informações sobre nome, telefone e data de vencimento
workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
 nome = linha[0].value
 telefone = linha[1].value
 vencimento = linha[2].value

 mensagem = f'Olá {nome} seu boleto vence no dia {vencimento.strftime()}. Favor pagar no link https://www.link_do_pagamento.com'

 # Criar links personalizados do whatsapp e enviar mensagens para cada cliente
 # com base nos dados da planilha
 try:
  link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
  webbrowser.open(link_mensagem_whatsapp)
  sleep(10)
  seta = pyautogui.locateCenterOnScreen('seta.png')
  sleep(2)
  pyautogui.click(seta[0], seta[1])
  sleep(2)
  pyautogui.hotkey('ctrl', 'w')
  sleep(2)
 except:
  print(f'Não foi possível enviar mensagem para {nome}')
  with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
   arquivo.write(f'{nome},{telefone}{os.linesep}')


"""
FUTURAMENTE CASO O USUARIO QUERIA AUTOMATIZAR TODO O PROCESSO DE COMPRA E ETC
"""

# def buyItem(url):
#
#  wd.get(item_to_purchase["URL"])
#  add_to_cart_button = wd.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
#  add_to_cart_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  no_thanks_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]')
#  no_thanks_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  view_cart_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]')
#  view_cart_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  #     not_interested_button = wd.find_element_by_xpath('//*[@id="Popup_Masks"]/div/div/div[3]/div[2]/button[1]')
#  #     not_interested_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  secure_checkout_button = wd.find_element_by_xpath(
#   '//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button')
#  secure_checkout_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  guest_checkout_button = wd.find_element_by_xpath(
#   '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/form[2]/div[2]/div/button')
#  guest_checkout_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  add_address = wd.find_element_by_xpath(
#   '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/i')
#  add_address.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  first_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[1]/input')
#  first_name.send_keys("Code")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  last_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[2]/input')
#  last_name.send_keys("Mental")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  address_first_line = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[6]/input')
#  address_first_line.send_keys("My house")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  city = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[8]/input')
#  city.send_keys("Broomfield")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  from selenium.webdriver.support.select import Select
#
#  state = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[9]/label[2]/select')
#  Select(state).select_by_value('CO')
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  zip_code = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[10]/input')
#  zip_code.clear()
#  zip_code.send_keys("80021")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  phone_number = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[12]/input')
#  phone_number.send_keys("1111111111")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  # email = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[15]/input')
#  # email.send_keys("codemental@example.com")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  save_button = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[2]')
#  save_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  use_address_as_entered = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[1]')
#  use_address_as_entered.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  go_to_delivery_button = wd.find_element_by_xpath(
#   '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[3]/button')
#  go_to_delivery_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  go_to_payment_page_button = wd.find_element_by_xpath(
#   '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button')
#  go_to_payment_page_button.click()
#
#  from selenium.common.exceptions import NoSuchElementException
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  while (True):
#   #    try:
#   url = "https://www.newegg.com/p/pl?N=100007709%20601357282"
#   items = checkForStock(url)
#   in_stock = items[(items["Item Price"] < 2500) & (items.Status == "Available")]
#   if not in_stock.empty:
#    item_to_purchase = in_stock.iloc[0]
#
#    buyItem(item_to_purchase["URL"])
#    break
#   else:
#    time.sleep(120)
#  #     except NoSuchElementException:
#  #         print("Out of stock")
#  #         print("waiting for some time....")
#  #         time.sleep(120)
#
#  # url = "https://www.newegg.com/p/pl?N=100007709%20601357248"
#  url = "https://www.newegg.com/p/pl?N=100007709%20601357282"
#  items = checkForStock(url)
#
#  items.info()
#
#  items[(items["Item Price"] < 2500) & (items.Status == "Available")]
#  items.head(1)["URL"].loc(0)
#
#  items.info()
#
#  items["Item Price"] = pd.to_numeric(items["Item Price"])
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  no_thanks_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]')
#  no_thanks_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  view_cart_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]')
#  view_cart_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  not_interested_button = wd.find_element_by_xpath('//*[@id="Popup_Masks"]/div/div/div[3]/div[2]/button[1]')
#  not_interested_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  secure_checkout_button = wd.find_element_by_xpath(
#   '//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button')
#  secure_checkout_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  guest_checkout_button = wd.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/form[2]/div[2]/div/button')
#  guest_checkout_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  add_address = wd.find_element_by_xpath(
#   '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/i')
#  add_address.click()
#
#  # ADC NOME DO USUARIO E IR PREENCHENDOOS VALORES DO CARRINHO
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  first_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[1]/input')
#  first_name.send_keys("Code")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  last_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[2]/input')
#  last_name.send_keys("Mental")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  address_first_line = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[6]/input')
#  address_first_line.send_keys("My house")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  city = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[8]/input')
#  city.send_keys("Broomfield")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  from selenium.webdriver.support.select import Select
#  state = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[9]/label[2]/select')
#  Select(state).select_by_value('CO')
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  zip_code = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[10]/input')
#  zip_code.clear()
#  zip_code.send_keys("80021")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  phone_number = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[12]/input')
#  phone_number.send_keys("1111111111")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  email = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[15]/input')
#  email.send_keys("codemental@example.com")
#
#  random_wait_time = random.randrange(5.0, 10.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  save_button = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[2]')
#  save_button.click()
#
#  # ENTREGA DE PRODUTO
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  use_address_as_entered = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[1]')
#  use_address_as_entered.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)
#
#  go_to_delivery_button = wd.find_element_by_xpath(
#   '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[3]/button')
#  go_to_delivery_button.click()
#
#  random_wait_time = random.randrange(5.0, 15.0)
#  print(random_wait_time)
#  time.sleep(random_wait_time)

 # go_to_payment_page_button = wd.find_element_by_xpath(
 #  '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button')
 # go_to_payment_page_button.click()