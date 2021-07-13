import requests
from datetime import datetime
import smtplib
import time

my_email = "bqshina1994@gmail.com"
password = "********"

MY_LAT = -37.813629
MY_LONG = 144.963058

while True:

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    # print(data)
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # Compare the position
    compare_long = longitude - MY_LONG
    compare_lat = latitude - MY_LAT
    print(compare_long)
    print(compare_lat)
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    # Get sunrise and sunset time
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 10
    if sunrise > 24:
        sunrise -= 24
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 10
    if sunset > 24:
        sunset -= 24

    time_now = datetime.now().hour

    if -5 <= compare_long <= 5 and -5 <= compare_lat <= 5 and \
            (time_now > sunset or time_now < sunrise):
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="bqshina@yahoo.com",
                            msg="Subject: Time to Look Up\n\nThe SSI is above you on the sky.")

    time.sleep(60)
