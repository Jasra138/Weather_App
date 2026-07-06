
import requests
from datetime import datetime

api_key = "c42e6e94f03c4c54851133341260607"

while True:

    print("\n" + "=" * 45)
    print("        🌦️ WEATHER APPLICATION 🌦️")
    print("=" * 45)

    city = input("Enter City Name: ")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "error" not in data:

        condition = data["current"]["condition"]["text"]

        if "Sunny" in condition:
            emoji = "☀️"
        elif "Cloud" in condition:
            emoji = "☁️"
        elif "Rain" in condition:
            emoji = "🌧️"
        elif "Thunder" in condition:
            emoji = "⛈️"
        elif "Snow" in condition:
            emoji = "❄️"
        else:
            emoji = "🌤️"

        print("\n" + "-" * 45)
        print(f"{emoji} WEATHER REPORT")
        print("-" * 45)
        print("📅 Date        :", datetime.now().strftime("%d-%m-%Y"))
        print("🕒 Time        :", datetime.now().strftime("%I:%M %p"))
        print("📍 City        :", data["location"]["name"])
        print("🌍 Country     :", data["location"]["country"])
        print("🌡 Temperature :", data["current"]["temp_c"], "°C")
        print("🤗 Feels Like  :", data["current"]["feelslike_c"], "°C")
        print("💧 Humidity    :", data["current"]["humidity"], "%")
        print("💨 Wind Speed  :", data["current"]["wind_kph"], "km/h")
        print("☁️ Condition   :", condition)
        print("-" * 45)

    else:
        print("\n❌", data["error"]["message"])

    choice = input("\nSearch another city? (y/n): ").lower()

    if choice != "y":
        print("\n🙏 Thank you for using Weather Application!")
        break