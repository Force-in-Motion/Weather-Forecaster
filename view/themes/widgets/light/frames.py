import customtkinter as ctk



class MainFrame(ctk.CTkFrame):
    def __init__(self, main):
        super().__init__(main, width = 800, height = 700, fg_color = 'white')
        self.pack_propagate(False)
        self.pack()



class CityWeatherFrame(ctk.CTkFrame):
    def __init__(self, main):
        super().__init__(main, fg_color='#cccccc', width=700, height=500, border_color='#18a5cc', border_width=1)
        self.pack_propagate(False)
        self.place(relx=0.07, rely=0.1)
