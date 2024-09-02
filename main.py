import customtkinter
from customtkinter import FontManager
from tkinter import *

URL = "http://127.0.0.1:8000/"


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x540")
app.title("Q'illu Clima")
app.resizable(False, False)


def button_function():
    if len(token_input.get()) == 50:
        message_input.
    else:
        message_input = "MUNDO"


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
    app, values=["Alta 800lx - 1400lx", "Media 600lx - 800lx", "Baja 200lx - 600lx"]
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
    app, values=["Alta 200mm - 500mm", "Media 50mm - 200mm", "Baja 0mm - 50mm"]
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
message_value = StringVar(value="................")
message_input = customtkinter.CTkLabel(
    app,
    textvariable=message_value,
    text_color="green",
)
message_input.place(x=15, y=400)


button2 = customtkinter.CTkButton(
    master=app, text="ENVIAR DATOS", command=button_function
)
button2.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()
