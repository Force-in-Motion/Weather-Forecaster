import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.__config_page()

    def __config_page(self):
        self.geometry('700x700')
        self.title('Weather Forecaster')

    @classmethod
    def run(cls):
        """
        Запускает главное окно приложения
        """
        page = cls()
        page.lift()
        page.attributes('-topmost', True)
        page.mainloop()