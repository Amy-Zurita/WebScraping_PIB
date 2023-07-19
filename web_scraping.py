import re

import requests
import pandas as pd
from bs4 import BeautifulSoup

fecha_list=[]
pib_eur_list=[]
pib_dol_list=[]
variacion_list=[]

url = 'https://datosmacro.expansion.com/pib/ecuador'

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')


tabla = soup.find('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'})
filas = tabla.find_all('tr')
for fila in filas:
     celdas = fila.find_all('td')
     if len(celdas) > 0:
         fecha = celdas[0].string
         pib_eur = re.sub(r'[^\d.]','', str(celdas[1].string))
         pib_dol =re.sub(r'[^\d.]','', str(celdas[2].string))
         variacion = celdas[3].string
         fecha_list.append(fecha)
         pib_eur_list.append(pib_eur)
         pib_dol_list.append(pib_dol)
         variacion_list.append(variacion)
df = pd.DataFrame({'Fecha':fecha_list, 'PIB (EUROS)':pib_eur_list, 'PIB (DOLARES)': pib_dol_list, 'Variacion': variacion_list})
df.to_csv('pib_ecu.csv', index=False, encoding='utf-8')

