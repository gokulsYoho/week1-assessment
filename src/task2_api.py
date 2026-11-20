import os
import csv
import json
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

all_emp = []
high_emp = []

with open("data/employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        all_emp.append(row)
        if int(row["salary"]) > 50000:
            high_emp.append(row)

with open("data/employees.json", "w") as jf:
    json.dump(all_emp, jf, indent=2)

with open("data/high_earners.csv", "w", newline="") as hf:
    writer = csv.DictWriter(hf, fieldnames=["id", "name", "department", "salary", "city"])
    writer.writeheader()
    writer.writerows(high_emp)

print(f"Rows read: {len(all_emp)} | High earners: {len(high_emp)}")

try:
    res = requests.get("https://typicode.com", timeout=5)
    users = res.json()

    for u in users[:3]:
        print(f"{u['id']} - {u['name']} - {u['email']}")

    saved_users = []
    for u in users:
        saved_users.append({
            "id": u.get("id"),
            "name": u.get("name"),
            "city": u.get("address", {}).get("city"),
            "company": u.get("company", {}).get("name")
        })

    with open("data/users.json", "w") as uf:
        json.dump(saved_users, uf, indent=2)

except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection failed")

try:
    res_404 = requests.get("https://typicode.com/9999", timeout=5)
    if res_404.status_code == 404:
        print("/users/9999 -> 404 Not found")
except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
    print("Connection error on /users/9999")
