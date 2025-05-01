import customtkinter as ctk
from controller.view_controller import DataController



class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.__controller = DataController(self)
        self.__current_theme = self.__controller.widgets
        self.__config_page()


    def __config_page(self) -> None:
        """
        Определяет конфигурацию главного окна приложения
        :return: None
        """
        self.geometry('800x700')
        self.title('Weather Forecaster')
        self.resizable(False, False)


    @classmethod
    def run(cls) -> None:
        """
        Запускает главное окно приложения.
        :return: None
        """
        page = cls()
        page.lift()
        page.attributes('-topmost', True)
        page.mainloop()