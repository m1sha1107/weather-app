from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Sweater Weather - Weather App using TKinter")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.config(cursor="heart")

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="SweaterWeather")
    location = geolocator.geocode(city)
    if location is None:
        raise("LOCATION NOT FOUND")
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude , lat=location.latitude)
    
    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("TIME: %I: %M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=e19cdbea726ed4c7ac11a4df461f41f6"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))    
    c.config(text=(condition,"","FEELS","LIKE",temp,"°"))



#search box
Search_image=PhotoImage(file="searchBar.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#9b5e37",border=0,fg="white")
textfield.place(x=40,y=50)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,bg="#9b5e37",command=getWeather)
myimage_icon.place(x=270,y=42)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=30,y=130)


#Bottom Box
Frame_image=PhotoImage(file="Box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(root,font=("arial",20,"bold"))
name.place(x=600,y=20)
clock = Label(root,font=("Helvetica",15))
clock.place(x=650,y=50)

#label
label1=Label(root,text="WIND", font=("Helvetica",10,'bold'),fg="white",bg="#e0b15e")
label1.place(x=230,y=350)

label2=Label(root,text="HUMIDITY", font=("Helvetica",10,'bold'),fg="white",bg="#e0b15e")
label2.place(x=330,y=350)

label3=Label(root,text="DESCRIPTION", font=("Helvetica",10,'bold'),fg="white",bg="#e0b15e")
label3.place(x=450,y=350)

label4=Label(root,text="PRESSURE", font=("Helvetica",10,'bold'),fg="white",bg="#e0b15e")
label4.place(x=600,y=350)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...", font=("arial",20,"bold"),bg="#e0b15e")
w.place(x=230,y=370)

h=Label(text="...", font=("arial",20,"bold"),bg="#e0b15e")
h.place(x=337,y=370)

d=Label(text="...", font=("arial",20,"bold"),bg="#e0b15e")
d.place(x=450,y=370)

p=Label(text="...", font=("arial",20,"bold"),bg="#e0b15e")
p.place(x=600,y=370)
root.mainloop()
