from tkinter import *
import requests
from datetime import datetime

root = Tk()

def get_weather():
    city = cityField.get()
    key = 'df90b50dc6d6065d7abf012f3d7a7e77'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': key, 'units': 'metric', 'lang': 'ru'}

    result = requests.get(url, params=params)
    weather = result.json()

    #если город не найден
    if weather.get('cod') != 200:
        info['text'] = 'Город не найден.'
        return

    temp = weather['main']['temp']
    description = weather['weather'][0]['description'].capitalize()
    sunrise = datetime.fromtimestamp(weather['sys']['sunrise']).strftime('%H:%M:%S')
    sunset = datetime.fromtimestamp(weather['sys']['sunset']).strftime('%H:%M:%S')

    info['text'] = (
        f"{description}\n"
        f"Температура: {temp}°C\n"
        f"Рассвет: {sunrise}\n"
        f"Закат: {sunset}"
    )

root['bg'] = '#fafafa'
root.title('Приложение для погоды')
root.geometry('675x585')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb334', bd = 5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.22)

frame_bottom = Frame(root, bg='#ffb334', bd=5)
frame_bottom.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.35)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

info = Label(frame_bottom, text='Погодная информация', bg='#ffb334', font=('Arial', 14), justify="center", anchor='nw')
info.pack(fill="both", expand=True, padx=9, pady=9)

root.mainloop()
