import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style
sns.set(style="whitegrid")

# Coordinates for London
latitude = 51.5074
longitude = -0.1278

# API (no key required)
url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'

# Fetch data
response = requests.get(url)
data = response.json()

# Extract current weather data
weather = data['current_weather']

# Create a dictionary for plotting
weather_metrics = {
    'Temperature (°C)': weather['temperature'],
    'Wind Speed (m/s)': weather['windspeed']
}

# Plot using seaborn and matplotlib
plt.figure(figsize=(8, 5))
sns.barplot(x=list(weather_metrics.keys()), y=list(weather_metrics.values()), palette='coolwarm')
plt.title('Current Weather in London', fontsize=16)
plt.ylabel('Value')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
