import customtkinter as ctk
from controller.view_controller import ThemeController



class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.__controller = ThemeController(self)
        self.__current_theme = self.__controller.widgets
        self.__config_page()


    def __config_page(self) -> None:
        """
        Определяет конфигурацию главного окна приложения
        :return: None
        """
        self.geometry('700x700')
        self.title('Weather Forecaster')
        self.resizable(False, False)


    def on_exit_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера.
        :return: None
        """
        self.destroy()


    @classmethod
    def run(cls) -> None:
        """
        Запускает главное окно приложения.
        :return: None
        """
        page = cls()

        # Привязка закрытия окна к методу on_exit_click
        page.protocol("WM_DELETE_WINDOW", page.on_exit_click)

        page.lift()
        page.attributes('-topmost', True)

        page.mainloop()