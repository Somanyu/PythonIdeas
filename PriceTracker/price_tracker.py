import requests
from bs4 import BeautifulSoup
import smtplib

URL = ' {URL of your Product} '

headers = {"User-Agent": 'headers of your browser'}


"""
 function that parses the product page for product name and price 
 and checks the price 
""" 
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if (converted_price < " {actual price of product} "):
        send_mail()

    print("Product: ", title.strip())
    print("Product's Price: ", converted_price)


"""
 function that sends email when product price decreases using SMTP protocol
"""
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('{your email ID} ', ' {App Password} ')

    subject = "Price Decreased on your Favourite Product on Amazon !!"

    body = 'Check this Amazon link {URL} '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        ' {From Email} ',
        ' {To Email}',
        msg
    )

    print("Email Sent Successfull!")

    server.quit()

check_price()