import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
print(APP_ID)
print(API_KEY)

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
sheet_headers = {
    "Authorization": f"Basic {os.getenv('TOKEN')}"
}

today = datetime.now()
day = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": input("Tell me which exercises you did: "),
}

app_response = requests.post(url=END_POINT, json=parameters, headers=headers)
exercises_data = app_response.json()["exercises"]


body = {
    "workout": {}
}

for exercise in exercises_data:
    exercise_record = {
        "date": day,
        "time": time,
        "exercise": exercise['name'],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
    body["workout"] = exercise_record
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=body, headers=sheet_headers)
    print(sheet_response.text)
