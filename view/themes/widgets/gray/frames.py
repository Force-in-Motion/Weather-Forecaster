import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    def __init__(self, main):
        super().__init__(main, fg_color='#787575', width=800, height=700)
        self.pack_propagate(False)
        self.pack()


class CityWeatherFrame(ctk.CTkFrame):
    def __init__(self, main):
        super().__init__(main, fg_color='#635959', width=700, height=500, border_color='#510973', border_width=1)
        self.pack_propagate(False)
        self.place(relx=0.07, rely=0.1)
