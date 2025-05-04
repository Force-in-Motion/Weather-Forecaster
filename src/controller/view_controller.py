from src.config.variables import *
from src.service.operations.db_operations import DBOperations
from src.service.model.facade import WeatherDataService
from src.model.weather_station import WeatherPublisher
from src.view.factory.dark import DarkThemeFactory
from src.view.factory.gray import GrayThemeFactory
from src.view.factory.light import LightThemeFactory

from src.tools.data_management import UpdateThreadLauncher as utl, FileLoader as fl


class DataController:
    """ Главный распределительный узел системы """

    def __init__(self, main):
        self.__main = main
        self.__current_theme = 'light'
        self.__db_service = DBOperations()
        self.__weather_service = WeatherDataService(fl.get_data(), CITY_LIST, self.__db_service)
        self.__loader = utl.loader(self.__weather_service.automatically_updates_db)
        self.__weather_station = WeatherPublisher(self.__weather_service)
        self.__widgets = self.__create_factory()


    def __create_factory(self) -> object:
        """
        Создает соответствующую фабрику на основе имени темы.
        :return: Экземпляр соответствующей фабрики.
        """
        if self.__current_theme == 'light':
            light = LightThemeFactory(self, self.__main, self.__weather_station)
            self.__weather_station.notification()
            return light

        elif self.__current_theme == 'dark':
            dark = DarkThemeFactory(self, self.__main, self.__weather_station)
            self.__weather_station.notification()
            return dark

        elif self.__current_theme == 'gray':
            gray = GrayThemeFactory(self, self.__main, self.__weather_station)
            self.__weather_station.notification()
            return gray


    def swap_theme(self, selected_theme: str) -> None:
        """
        Переключает тему на основе выбранного значения из combobox`s.
        Уничтожает существующие виджеты и создает новые для новой темы.
        :param selected_theme: Текущая выбранная тема.
        :return: None
        """
        for subscriber in self.__weather_station.subscribers[:]:
            subscriber.unsubscribe()

        for widget in self.__main.winfo_children():
            widget.destroy()

        self.__current_theme = selected_theme

        self.__widgets = self.__create_factory()


    def on_update_click(self) -> None:
        """
        Обрабатывает клик по кнопке обновления текстовых данных в лейблах главной страницы
        :return:
        """
        self.__weather_station.notification()


    def on_exit_click(self) -> None:
        """
        Обрабатывает клик по кнопке выхода из программы
        :return: None
        """
        self.__main.destroy()


    @property
    def widgets(self):
        """
        Возвращает все виджеты, соответствующее выбранной теме
        :return:
        """
        return self.__widgets




