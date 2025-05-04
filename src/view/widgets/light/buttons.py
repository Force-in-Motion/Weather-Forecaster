import customtkinter as ctk



class UpdateButton(ctk.CTkButton):
    """ Формирует объект кнопки, отвечающей за обновление данных в лейблах """

    def __init__(self, main_frame, weather_station):
        super().__init__(main_frame,
                         width=200,
                         height=50,
                         text='Update',
                         text_color='black',
                         fg_color='#1d87b5',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#1779a3',
                         command=weather_station.notification)

        self.place(relx=0.55, rely=0.85)



class ExitButton(ctk.CTkButton):
    """ Формирует объект кнопки, отвечающей за выход из программы """

    def __init__(self, main_frame, main):
        super().__init__(main_frame,
                         width=200,
                         height=50,
                         text='Close',
                         text_color='black',
                         fg_color='#1d87b5',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#1779a3',
                         command=main.on_exit_click)

        self.place(relx=0.2, rely=0.85)
