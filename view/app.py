import customtkinter as ctk
from view.widgets import LightFactory, DarkFactory, GrayFactory
from config.city import city_list
from config.themes import themes


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.__current_theme = 'Light'  # Отслеживание текущей темы
        self.__config_page()
        self.__create_factory()  # Создание начальных виджетов

    def __config_page(self):
        self.geometry('700x700')
        self.title('Weather Forecaster')
        self.resizable(False, False)

    def __create_factory(self):
        """
        Создает соответствующую фабрику на основе имени темы.
        :return: Экземпляр соответствующей фабрики.
        """
        if self.__current_theme == 'Light':
            return LightFactory(self, city_list)

        elif self.__current_theme == 'Dark':
            return DarkFactory(self, city_list)

        elif self.__current_theme == 'Gray':
            return GrayFactory(self, city_list)

    def swap_theme(self, selected_theme):
        """
        Переключает тему на основе выбранного значения из комбобокса.
        Уничтожает существующие виджеты и создает новые для новой темы.
        :param selected_theme: Текущая выбранная тема.
        """

        for widget in self.winfo_children():
            widget.destroy()

        # Установка текущей темы на основе выбора в комбобоксе
        self.__current_theme = selected_theme

        # Создание новой фабрики и виджетов для новой темы
        self.__create_factory()


    def on_exit_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера.
        :return: None
        """
        self.destroy()


    @classmethod
    def run(cls):
        """
        Запускает главное окно приложения.
        """
        page = cls()

        # Привязка закрытия окна к методу on_exit_click
        page.protocol("WM_DELETE_WINDOW", page.on_exit_click)

        page.lift()
        page.attributes('-topmost', True)

        page.mainloop()