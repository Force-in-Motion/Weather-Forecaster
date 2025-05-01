from config.variables import *
from service.operations.db_operations import DBOperations
from tools.load_data import LoadData as ld
from model.weather_station import WeatherPublisher
from view.themes.factory.dark import DarkThemeFactory
from view.themes.factory.gray import GrayThemeFactory
from view.themes.factory.light import LightThemeFactory
from service.model.facade import WeatherDataService


class DataController:

    def __init__(self, main):
        self.__main = main
        self.__current_theme = 'Light'
        self.__db_service = DBOperations()
        self.__weather_service = WeatherDataService(ld.get_data(), CITY_LIST, self.__db_service)
        self.__loader = ld.loader(self.__weather_service.automatically_updates_db)
        self.__weather_station = WeatherPublisher(self.__weather_service)
        self.__widgets = self.__create_factory()
        self.__weather_station.notification()


    def __create_factory(self) -> object:
        """
        Создает соответствующую фабрику на основе имени темы.
        :return: Экземпляр соответствующей фабрики.
        """

        if self.__current_theme == 'Light':
            return LightThemeFactory(self, self.__main, self.__weather_station)

        elif self.__current_theme == 'Dark':
            return DarkThemeFactory(self, self.__main, self.__weather_station)

        elif self.__current_theme == 'Gray':
            return GrayThemeFactory(self, self.__main, self.__weather_station)


    def swap_theme(self, selected_theme) -> None:
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


    def on_update_click(self):
        self.__weather_station.notification()


    def on_exit_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера.
        :return: None
        """
        self.__main.destroy()


    @property
    def widgets(self):
        return self.__widgets




