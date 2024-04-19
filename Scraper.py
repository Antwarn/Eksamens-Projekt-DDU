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
headers = ['Time', 'Company', 'Price', 'Volume', 'Market Cap']

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
                price = float(price_text)
        
            close_price_element = soup.find('span', {'class': 'key-info_dd-numeric__ZQFIs'})
            if close_price_element:
                close_price_text = close_price_element.text
                close_price = float(close_price_text)
            volume_element = soup.find_all(class_ = 'key-info_dd-numeric__ZQFIs')

            if volume_element:
                volumen_text = volume_element[9].text.replace(',','')
                volume = float(volumen_text)

            market_cap = close_price * volume

            stock_info = [tidskode, company, price, volume, market_cap]
            print(stock_info)

            writer.writerow([tidskode, company, price ,volume, market_cap])
    
    time.sleep(10)   