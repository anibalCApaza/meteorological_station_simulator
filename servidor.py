import customtkinter
import time
import random
import requests
from customtkinter import FontManager
from tkinter import *


URL = "http://134.209.168.118/actualizar_lectura"


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x540")
app.title("Q'illu Clima")
app.resizable(False, False)


def button_function():
    len_token = len(token_input.get().strip())

    if (len_token == 50):
        message_input.configure(
            text='Enviando datos con el token '+token_input.get())
        token = token_input.get().strip()

        match temperature_combo_box.get():
            case "Calido (20°C-30°C)":
                t = round(random.uniform(20.0, 30.0), 2)
            case "Normal (10°C-20°C)":
                t = round(random.uniform(10.0, 20.0), 2)

            case "Frio (0°C-10°C)":
                t = round(random.uniform(0.0, 10.0), 2)

        match humidity_combo_box.get():
            case "Alta 80% - 100%":
                h = round(random.uniform(80.0, 100.0), 2)
            case "Medio 60% - 80%":
                h = round(random.uniform(60.0, 80.0), 2)
            case "Baja 30% - 60%":
                h = round(random.uniform(30.0, 60.0), 2)

        match luminity_combo_box.get():
            case "Alta 10000lx - 15000lx":
                l = round(random.uniform(10000.0, 15000.0), 2)
            case "Media 1000lx - 10000lx":
                l = round(random.uniform(1000.0, 10000.0), 2)
            case "Baja 10lx - 1000lx":
                l = round(random.uniform(10.0, 1000.0), 2)

        match precipitation_combo_box.get():
            case "Alta 2mm - 4mm":
                p = round(random.uniform(2.0, 4.0), 2)
            case "Media 1mm - 2mm":
                p = round(random.uniform(1.0, 2.0), 2)
            case "Baja 0mm - 1mm":
                p = round(random.uniform(0.0, 1.0), 2)
        i = 1
        while True:
            tem = round(t+random.uniform(0.0, 1.5), 2)
            hum = round(h+random.uniform(0.0, 3.0), 2)
            lum = round(l+random.uniform(0.0, 100.0), 2)
            pre = round(p+random.uniform(0.0, 0.5), 2)

            params = {
                'temperature': tem,
                'humidity': hum,
                'luminosity': lum,
                'precipitation': pre,
                'token': token
            }

            response = requests.put(URL, params=params)

            print(f'{i} - Status Code: {response.status_code}')

            try:
                print(f'Response: {response.json()}')
            except requests.exceptions.JSONDecodeError:
                print('Response is not in JSON format')

            time.sleep(5)
            i = i + 1

    else:
        message_input.configure(
            text='Error de Token, debe tener una longitud de 50 y actualmente es de ' +
            str(len_token)
        )


def clear_token():
    token_input.delete(0, END)


app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

# titulo
title = customtkinter.CTkLabel(
    master=app,
    text="SIMULADOR DE ESTACIÓN METEOROLÓGICA Q'ILLU CLIMA",
    font=customtkinter.CTkFont(
        family="Helvetica",
        size=18,
        weight="bold",
    ),
    text_color="orange",
)
title.place(x=40, y=10)

# elementos para temperatura
temperature_label = customtkinter.CTkLabel(
    master=app,
    text="TEMPERATURA:",
    font=customtkinter.CTkFont(weight="bold"),
    text_color="#E5FFCC",
)
temperature_label.place(x=30, y=70)

temperature_combo_box = customtkinter.CTkComboBox(
    app, values=["Calido (20°C-30°C)", "Normal (10°C-20°C)", "Frio (0°C-10°C)"]
)
temperature_combo_box.place(x=150, y=70)

# elementos para humedad
humidity_label = customtkinter.CTkLabel(
    master=app,
    text="HUMEDAD REL:",
    font=customtkinter.CTkFont(weight="bold"),
    text_color="#E5FFCC",
)
humidity_label.place(x=310, y=70)

humidity_combo_box = customtkinter.CTkComboBox(
    app, values=["Alta 80% - 100%", "Medio 60% - 80%", "Baja 30% - 60%"]
)
humidity_combo_box.place(x=420, y=70)


#  Elementos de luminosidad
luminity_label = customtkinter.CTkLabel(
    master=app,
    text="LUMINOSIDAD:",
    font=customtkinter.CTkFont(weight="bold"),
    text_color="#E5FFCC",
)
luminity_label.place(x=30, y=180)

luminity_combo_box = customtkinter.CTkComboBox(
    app, values=["Alta 10000lx - 15000lx",
                 "Media 1000lx - 10000lx", "Baja 10lx - 1000lx"]
)
luminity_combo_box.place(x=150, y=180)

# Elementos de Precipitación Pluvial

precipitation_label = customtkinter.CTkLabel(
    master=app,
    text="PRECIPITACIÓN:",
    font=customtkinter.CTkFont(weight="bold"),
    text_color="#E5FFCC",
)
precipitation_label.place(x=300, y=180)

precipitation_combo_box = customtkinter.CTkComboBox(
    app, values=["Alta 2mm - 4mm", "Media 1mm - 2mm", "Baja 0mm - 1mm"]
)
precipitation_combo_box.place(x=420, y=180)

# ELEMENTOS PARA TOKEN
token_label = customtkinter.CTkLabel(
    master=app,
    text="TOKEN:",
)
token_label.place(x=30, y=300)

token_input = customtkinter.CTkEntry(
    app, placeholder_text="Inserte el token", width=350
)
token_input.place(x=100, y=300)

token_clear_button = customtkinter.CTkButton(
    app,
    text="LIMPIAR",
    command=clear_token,
    width=70,
    fg_color="red",
    hover_color="orange",
)
token_clear_button.place(x=470, y=300)


# Mensaje
message_input = customtkinter.CTkLabel(
    app,
    text='................',
    text_color="green",
)
message_input.place(x=15, y=400)


button2 = customtkinter.CTkButton(
    master=app, text="ENVIAR DATOS", command=button_function
)
button2.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()
