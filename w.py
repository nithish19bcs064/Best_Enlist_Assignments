from tkinter import *
import tkinter as tk
import requests


HEIGHT = 500
WIDTH = 500

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']



		if Cbutton:
			final_str = 'Place: %s \nWeather: %s \nTemperature: %s' % (name, desc, temp)


	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'Imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

def get_weatherM(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg='light grey')
canvas.pack()

frame = tk.Frame(root, bg='Gray', bd=25)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n',)

entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.5, relheight=1)



Cbutton = tk.Button(frame, text="Fetch Tempearture", font='times 13', command=lambda: get_weatherM(entry.get()))
Cbutton.place(relx=0.6,rely=0,relheight=1, relwidth=0.45)

lower_frame = tk.Frame(root, bg='Grey', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()