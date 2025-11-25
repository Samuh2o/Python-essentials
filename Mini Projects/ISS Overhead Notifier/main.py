import requests
from datetime import datetime
import smtplib
from time import sleep

MY_LAT = -23.694450 # Your latitude
MY_LONG = -46.565800 # Your longitude
SENDER_EMAIL = "samuelhermsdorff@gmail.com"
PASSWORD = "PASSWORD"
EMAIL_PORT = 587
EMAIL_HOST = "smtp.gmail.com"
RECEIVER_EMAIL = "samuel.hermsdorff@aluno.ufabc.edu.br"

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
    except requests.exceptions.ConnectTimeout:
        pass
    else:
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True

def is_night():
    parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", timeout=10, params=parameters)
    except requests.exceptions.ConnectTimeout:
        pass
    else:
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now().hour
        
        if time_now >= sunset or time_now <= sunrise:
            return True 
        
while True:
    #If the ISS is close to my current position
    # and it is currently dark
    sleep(60)
    if is_iss_overhead() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP(EMAIL_HOST, port=EMAIL_PORT) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg="Subject:Look up!\n\nThe ISS is above you in the sky!"
            )
