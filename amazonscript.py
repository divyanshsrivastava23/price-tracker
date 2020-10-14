import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/dp/B07DJHXTLJ/ref=gwdb_bmc_0_OnePlus%207T?pf_rd_s=merchandised-search-5&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=N312492DHHVV9NT1M2S1&pf_rd_p=776d2e5b-b124-4643-9c3d-e746ebcde5ab'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:].replace(',',''))
    if converted_price < 34999.0:
        send_mail()

    print(title.strip())
    print(converted_price)
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('srivastavadivyansh633@gmail.com' , 'ojkdpmbmlkqaqgyq')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/dp/B07DJHXTLJ/ref=gwdb_bmc_0_OnePlus%207T?pf_rd_s=merchandised-search-5&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=N312492DHHVV9NT1M2S1&pf_rd_p=776d2e5b-b124-4643-9c3d-e746ebcde5ab'
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'your-email',
        msg
    )
    print('Mail Sent!!!')
    server.quit()
check_price()