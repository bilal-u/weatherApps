import tkinter as tk
from tkinter import ttk
#from tkinter import *

import requests
# ab
# user defined functions

def get_weather_forecast(city="st. john's"):
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    api_key = "66dcb3a3b6a02250c807dbe33ba6ea95"
    url = f'{base_url}q={city}&appid={api_key}'
    resp = requests.get(url)
    return resp

def get_all_weather_data(city="st. john's"):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "66dcb3a3b6a02250c807dbe33ba6ea95"
    url = f'{base_url}q={city}&appid={api_key}'
    resp = requests.get(url)
    return resp

def get_current_temp(city):
    # return temp in Celsius
    data = get_all_weather_data(city).json()
    current_temp = data['main']['temp']
    return round(current_temp - 273.15)

def get_current_feels_like_temp(city):
    # return temp in Celsius
    data = get_all_weather_data(city).json()
    current_feels_like = data['main']['feels_like']
    return round(current_feels_like - 273.15)

def get_current_summary(city):
    # get weather summary
    data = get_all_weather_data(city).json()
    current_weather_summary = data['weather'][0]['description']
    return current_weather_summary

def get_current_wind_speed(city):
    # return wind speed in km/h
    data = get_all_weather_data(city).json()
    current_wind_speed = data['wind']['speed']
    return round(current_wind_speed*(18/5))

def get_current_wind_gusts(city):
    # return wind gusts in km/h
    data = get_weather_forecast(city).json()
    current_wind_gusts = data['list'][0]['wind']['gust']
    return round(current_wind_gusts*(18/5))


def main():
    city = city_name.get()
    resp = get_all_weather_data(city)
    if resp.status_code == 200:
        curr_temp = get_current_temp(city)
        current_temp.set(f'{curr_temp} Cel')

        curr_feels_like = get_current_feels_like_temp(city)
        feels_like_temp.set(f'{curr_feels_like} Cel')

        summ_data = get_current_summary(city)
        summary_data.set(summ_data)

        curr_wind_speed = get_current_wind_speed(city)
        wind_speed.set(f'{curr_wind_speed} Km/h')

        curr_wind_gusts = get_current_wind_gusts(city)
        wind_gusts.set(f'{curr_wind_gusts} Km/h')
    elif resp.status_code == 404:
        print(f'city {city} not found!')


# Create the root window

root = tk.Tk()
root.title('My Weather App')
root.geometry('500x300')
root.geometry('700x300')


# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)


# Create a label
ttk.Label(frame_home, text="My Weather App").grid(row=0, column=2)

ttk.Label(frame_home, text="Enter City: ").grid(column=0, row=1)

# Create an entry box
city_name = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=city_name).grid(column=1, row=1)

# button for get weather info
get_weather=ttk.Button(frame_home, text="Get Current Weather",command = lambda: main()).grid(column=1,row = 2)

# labels for current weather info
ttk.Label(frame_home, text="Current Temp: ").grid(column=1, row=3)
ttk.Label(frame_home, text="Feels Like Temp: ").grid(column=1, row=4)
ttk.Label(frame_home, text="Summary: ").grid(column=1, row=5)
ttk.Label(frame_home, text="Wind Speed: ").grid(column=1, row=6)
ttk.Label(frame_home, text="Wind Gusts: ").grid(column=1, row=7)

# entry boxes
current_temp = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=current_temp,state='readonly').grid(column=2, row=3)

feels_like_temp = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=feels_like_temp,state='readonly').grid(column=2, row=4)

summary_data = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=summary_data,state='readonly').grid(column=2, row=5)

wind_speed = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=wind_speed,state='readonly').grid(column=2, row=6)

wind_gusts = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=wind_gusts,state='readonly').grid(column=2, row=7)

root.mainloop()


if __name__ == '__main__':
    main()
