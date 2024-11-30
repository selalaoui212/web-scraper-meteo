import requests

API_KEY = "votre_clé_api"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Entrez le nom de la ville : ")

complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"

response = requests.get(complete_url)


data = response.json()

if data["cod"] != 200:
    print(f"Erreur: {data['message']}")
else:
    main_data = data.get("main", {})
    weather_data = data.get("weather", [{}])[0]

    if main_data and weather_data:
        temperature = main_data.get("temp")
        humidity = main_data.get("humidity")
        weather_description = weather_data.get("description")

        print(f"\nMétéo pour {city_name}:")
        print(f"Température : {temperature}°C")
        print(f"Humidité : {humidity}%")
        print(f"Description : {weather_description.capitalize()}")
    else:
        print("Les données météorologiques ne sont pas disponibles.")
