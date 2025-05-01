import customtkinter as ctk



class UpdateButton(ctk.CTkButton):
    def __init__(self, main_frame, weather_station):
        super().__init__(main_frame,
                         width=200,
                         height=50,
                         text='Update',
                         text_color='black',
                         fg_color='#18a5cc',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#117996',
                         command=weather_station.notification)

        self.place(relx=0.55, rely=0.85)



class ExitButton(ctk.CTkButton):
    def __init__(self, main_frame, main):
        super().__init__(main_frame,
                         width=200,
                         height=50,
                         text='Close',
                         text_color='black',
                         fg_color='#18a5cc',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#117996',
                         command=main.on_exit_click)

        self.place(relx=0.2, rely=0.85)
