from interface.widget_factory import AWidgetFactory

from view.widgets.light.combobox import SwapCbox
from view.widgets.light.buttons import UpdateButton, ExitButton
from view.widgets.light.frames import MainFrame, WeatherSubscribersFrame
from view.widgets.light.labels import TitleLabel, WeatherSubscriber


class LightThemeFactory(AWidgetFactory):
    """ Фабрика виджетов темной темы """

    def __init__(self, controller, main, weather_station):
        super().__init__(main)
        self.__controller = controller
        self.__weather_station = weather_station
        self._create_main_frame()
        self._create_city_weather_frame()
        self._create_update_button()
        self._create_exit_button()
        self._create_swap_cbox()
        self._create_title_label()
        self._create_city_weather_label()


    def _create_main_frame(self) -> None:
        """
        Создает главный фрейм приложения
        :return: None
        """
        self._main_frame = MainFrame(self._main)


    def _create_city_weather_frame(self) -> None:
        """
        Создает фрейм приложения, содержащий лейблы с данными о погоде
        :return: None
        """
        self._city_weather_frame = WeatherSubscribersFrame(self._main_frame)


    def _create_update_button(self) -> None:
        """
        Создает кнопку обновления данных в лейблах с данными о погоде
        :return: None
        """
        self._update_btn = UpdateButton(self._main_frame, self.__weather_station)


    def _create_exit_button(self) -> None:
        """
        Создает кнопку выхода из приложения
        :return: None
        """
        self._exit_btn = ExitButton(self._main_frame, self.__controller)


    def _create_swap_cbox(self) -> None:
        """
        Создает Combobox, содержащий названия тем для переключения
        :return: None
        """
        self._swap_theme_cbox = SwapCbox(self._main_frame, self.__controller)


    def _create_title_label(self) -> None:
        """
        Создает главный текстовый лейбл приложения
        :return: None
        """
        self._title = TitleLabel(self._main_frame)


    def _create_city_weather_label(self) -> None:
        """
        Создает лейблы с данными о погоде
        :return: None
        """
        for _ in self.__weather_station.count:
            self._city_weather_label = WeatherSubscriber(self._city_weather_frame, self.__weather_station)