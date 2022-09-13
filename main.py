import time

import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.de/SPGOOD-trainingsger%C3%A4t-Liegest%C3%BCtzbrett-einzirartige-Professionell/dp/B08CBVNDPG" \
      "/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=push+up&qid=1637346612&qsid=257-7151513" \
      "-1676541&sr=8-5&sres=B08CBVNDPG%2CB008XY49UM%2CB0888D1TK6%2CB07R4LTL4H%2CB083RW7S8C%2CB073J126J7%2CB0855QN6DT" \
      "%2CB08HQTL166%2CB08T7CZZFY%2CB08MD6YSF6%2CB0854B5V6H%2CB09F3G4NPX%2CB08TC11FNN%2CB08R9DJ5G8%2CB088WWX7G2" \
      "%2CB00BN7E8R0%2CB003ES4YMA%2CB07JVV9W6J%2CB01GILX240%2CB07Q9TSHNN "

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"}


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("andreascalleja@gmail.com", "ghqkyvftdrorhvef")
    subject = "Price Fall"
    body = f"Check amazon link {url}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "andreascalleja@gmail.com",
        "andreascalleja@gmail.com",
        msg
    )

    print("Mail sent")
    server.quit()


def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text().strip()
    price = float(soup.find(class_="a-offscreen").get_text()[:-1].replace(",", "."))

    if price < 20:
        send_mail()


while True:
    check_price()
    time.sleep(3600)
