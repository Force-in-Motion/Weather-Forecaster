import customtkinter as ctk



class MainFrame(ctk.CTkFrame):
    """ Формирует объект главного фрейма приложения """

    def __init__(self, main):
        super().__init__(main, width = 800, height = 700, fg_color = 'white')
        self.pack_propagate(False)
        self.pack()



class WeatherSubscribersFrame(ctk.CTkFrame):
    """ Формирует объект фрейма, содержащий лейблы с данными о погоде """

    def __init__(self, main):
        super().__init__(main, fg_color='#cccccc', width=700, height=500, border_color='#1d87b5', border_width=1)
        self.pack_propagate(False)
        self.place(relx=0.07, rely=0.1)
