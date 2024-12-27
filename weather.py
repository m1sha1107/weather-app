from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Sweater Weather - Weather App using Tkinter")
root.geometry("900x500+300+200")
root.resizable(False, False)
root.config(cursor="heart")

def getWeather():
    city = textfield.get()

    try:
        geolocator = Nominatim(user_agent="SweaterWeather")
        location = geolocator.geocode(city)

        if not location:
            messagebox.showerror("Error", "Location not found!")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("TIME: %I:%M %p")
        clock.config(text=current_time)
        name.config(text=f"CURRENT WEATHER IN \n {city.upper()}")

        # Weather API
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=e19cdbea726ed4c7ac11a4df461f41f6"
        json_data = requests.get(api).json()

        # Extracting weather data
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)  #convert from Kelvin to Celsius
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Updating UI
        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | Feels like {temp}°C")
        w.config(text=f"{wind} km/h")
        h.config(text=f"{humidity}%")
        d.config(text=description.capitalize())
        p.config(text=f"{pressure} hPa")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Search box
Search_image = PhotoImage(file="searchBar.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=15, font=("Times New Roman", 25, "bold"), bg="#9b5e37", border=0, fg="white")
textfield.place(x=40, y=50)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, bg="#9b5e37", command=getWeather)
myimage_icon.place(x=270, y=42)

# Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=30, y=130)

# Bottom Box
Frame_image = PhotoImage(file="Bottom.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("Times New Roman", 20, "bold"))
name.place(x=500, y=20)
clock = Label(root, font=("Times New Roman", 15))
clock.place(x=600, y=100)

# Labels
label1 = Label(root, text="WIND", font=("Times New Roman", 10, 'bold'), fg="white", bg="#ac663e")
label1.place(x=200, y=400)

label2 = Label(root, text="HUMIDITY", font=("Times New Roman", 10, 'bold'), fg="white", bg="#ac663e")
label2.place(x=330, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Times New Roman", 10, 'bold'), fg="white", bg="#ac663e")
label3.place(x=500, y=400)

label4 = Label(root, text="PRESSURE", font=("Times New Roman", 10, 'bold'), fg="white", bg="#ac663e")
label4.place(x=700, y=400)

t = Label(font=("Times New Roman", 70, "bold"), fg="#e0b15e")
t.place(x=400, y=150)

c = Label(font=("Times New Roman", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 15, "bold"), bg="#ac663e")
w.place(x=200, y=430)

h = Label(text="...", font=("arial", 15, "bold"), bg="#ac663e")
h.place(x=330, y=430)

d = Label(text="...", font=("arial",15, "bold"), bg="#ac663e")
d.place(x=470, y=430)

p = Label(text="...", font=("arial", 15, "bold"), bg="#ac663e")
p.place(x=700, y=430)

root.mainloop()
