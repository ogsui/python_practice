capital_city = {
    "INDIA": "New Delhi",
    "USA": "Washington D.C.",
    "UNITEDSTATESOFAMERICA": "Washington D.C.",
    "JAPAN": "Tokyo"
}

country = input("Enter country name: ").strip().upper()
if country in capital_city:
    print(f"{capital_city[country]}")
else:
    print("invalid")