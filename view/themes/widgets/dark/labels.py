import customtkinter as ctk



class TitleLabel(ctk.CTkLabel):

    def __init__(self, master):
        super().__init__(master,
                         width=400,
                         height=60,
                         font=('Helvetica', 24, 'bold'),
                         fg_color="transparent",
                         justify='center',
                         text='Weather forecast by city',
                         text_color='#ad321c')

        self.place(relx=0.2, rely=0.01)



class CityWeatherLabel(ctk.CTkLabel):

    def __init__(self, master, city):
        super().__init__(master,
                         text_color='#a7a5a8',
                         anchor='w',
                         font=('Helvetica', 18, 'bold'),
                         text=f'{city} - Температура: ')

        self.pack(fill='x', padx=10, pady=14)

