import pandas as pd
import requests
import os
from io import StringIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_sfs():
options = Options()
    options.add_argument('--headless=new') 
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    # User-Agent
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get("https://praticagemsf.com.br/movimentacoes/")
        wait = WebDriverWait(driver, 25)
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'portal')]")))
        driver.switch_to.frame(iframe)
        tabela_el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tabReg")))
        df = pd.read_html(StringIO(tabela_el.get_attribute('outerHTML')))[0]
        driver.quit()
        df.columns = ['Navio', 'IMO', 'Tipo', 'Agência', 'Comp', 'Boca', 'Calado', 'GRT', 'Callsign', 'Chegada', 'Ult_Manobra', 'Manobra', 'Data_Manobra', 'Berço', 'Situação']
        df['Origem'] = 'SFS/Itapoá (ZP-18)'
        return df
    except:
        driver.quit()
        return pd.DataFrame()

def get_itj():
    url = "https://praticoszp21.com.br/movimentacao-de-navios/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        df = pd.read_html(StringIO(r.text))[0]
        df['Origem'] = 'Itajaí/NVT (ZP-21)'
        return df
    except:
        return pd.DataFrame()

# Execução
df_hoje = pd.concat([get_sfs(), get_itj()], ignore_index=True, sort=False)
nome_csv = "banco_dados_movimentacao.csv"

if os.path.exists(nome_csv):
    df_hist = pd.read_csv(nome_csv)
    df_final = pd.concat([df_hist, df_hoje], ignore_index=True).drop_duplicates(subset=['Navio', 'Manobra', 'Berço'], keep='first')
else:
    df_final = df_hoje

df_final.to_csv(nome_csv, index=False, encoding='utf-8-sig')
print(f"Banco atualizado com {len(df_final)} registros.")
