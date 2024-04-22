import os.path
import requests
from bs4 import BeautifulSoup
import csv
import time

urls = [
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/netflix,-inc.',
    'https://www.investing.com/equities/polo-ralph-laur',
    'https://www.investing.com/equities/google-inc',
    'https://www.investing.com/equities/nvidia-corp'
]

csv_filename = 'stockinfo.csv'
headers = ['Time','Open', 'High', 'Low', 'Last','Close' ,'Volume']

while True:
    tidskode = time.strftime('%Y-%m-%d %H:%M:%S')

    # Check if file exists
    file_exists = os.path.isfile(csv_filename)

    # Open CSV file in append mode
    with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # If file doesn't exist, write headers
        if not file_exists:
            writer.writerow(headers)

        for url in urls:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            company = soup.find('h1', {'class': 'mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr'}).text.strip()
            price_element = soup.find('div', {'class': 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'})
            if price_element:
                price_text = price_element.text
                Last = float(price_text)
        
            close_price_element = soup.find('span', {'class': 'key-info_dd-numeric__ZQFIs'})
            if close_price_element:
                close_price_text = close_price_element.text
                Close = float(close_price_text)

            volume_element = soup.find_all(class_ = 'key-info_dd-numeric__ZQFIs')
            if volume_element:
                volumen_text = volume_element[9].text.replace(',','')
                volume = float(volumen_text)

            Open_price_element = soup.find_all(class_ = 'key-info_dd-numeric__ZQFIs')
            if Open_price_element:
                Open_price_text = Open_price_element[1].text.replace(',','')
                Open = float(Open_price_text)

            High_price_element = soup.find_all(class_ = 'key-info_dd-numeric__ZQFIs')
            if High_price_element:
                High_price_text = High_price_element[3].text.replace(',','')
                High = float(High_price_text)

            Low_price_element = soup.find_all(class_ = 'key-info_dd-numeric__ZQFIs')
            if Low_price_element:
                Low_price_text = Low_price_element[2].text.replace(',','')
                Low = float(Low_price_text)

            market_cap = Close * volume

            stock_info = [tidskode, company, Open, High, Low, Last, Close, volume, market_cap]
            print(Low)

            writer.writerow([tidskode, Open, High, Low, Last, Close, volume])
    
    time.sleep(10)   