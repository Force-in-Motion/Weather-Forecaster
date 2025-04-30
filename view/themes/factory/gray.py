from interface.widget_factory import AWidgetFactory

from view.themes.widgets.gray.combobox import SwapCbox
from view.themes.widgets.gray.buttons import UpdateButton, ExitButton
from view.themes.widgets.gray.frames import MainFrame, CityWeatherFrame
from view.themes.widgets.gray.labels import TitleLabel, CityWeatherLabel



class GrayThemeFactory(AWidgetFactory):

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
        self._main_frame = MainFrame(self._main)


    def _create_city_weather_frame(self) -> None:
        self._city_weather_frame = CityWeatherFrame(self._main_frame)


    def _create_update_button(self) -> None:
        self._update_btn = UpdateButton(self._main_frame, self.__weather_station)


    def _create_exit_button(self) -> None:
        self._exit_btn = ExitButton(self._main_frame, self._main)

    def _create_swap_cbox(self) -> None:
        self._swap_theme_cbox = SwapCbox(self._main_frame, self.__controller)


    def _create_title_label(self) -> None:
        self._title = TitleLabel(self._main_frame)


    def _create_city_weather_label(self):
        for _ in self.__weather_station.count:
            self._city_weather_label = CityWeatherLabel(self._city_weather_frame, self.__weather_station)
