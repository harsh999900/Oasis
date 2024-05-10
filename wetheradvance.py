import requests
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        
        self.label_city = tk.Label(master, text="Enter city name:")
        self.label_city.grid(row=0, column=0)
        self.entry_city = tk.Entry(master)
        self.entry_city.grid(row=0, column=1)
        
        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=1, columnspan=2)
        
        self.weather_info_label = tk.Label(master, text="")
        self.weather_info_label.grid(row=2, columnspan=2)
        
    def get_weather(self):
        city = self.entry_city.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return
        
        api_key = "bd5e378503939ddaee76f12ad7a97608"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            weather_info = f"Current Weather in {data['name']}\n"
            weather_info += f"Temperature: {data['main']['temp']} °C\n"
            weather_info += f"Humidity: {data['main']['humidity']}%\n"
            weather_info += f"Weather: {data['weather'][0]['description']}"
            self.weather_info_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", data["message"])

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
