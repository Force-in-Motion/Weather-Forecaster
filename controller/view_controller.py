
from config.cities import city_list
from view.themes.factory.dark import DarkThemeFactory
from view.themes.factory.gray import GrayThemeFactory
from view.themes.factory.light import LightThemeFactory


class ThemeController:

    def __init__(self, main):
        self.__main = main
        self.__current_theme = 'Light'
        self.__widgets = self.__create_factory()


    def __create_factory(self) -> object:
        """
        Создает соответствующую фабрику на основе имени темы.
        :return: Экземпляр соответствующей фабрики.
        """
        if self.__current_theme == 'Light':
            return LightThemeFactory(self, self.__main, city_list)

        elif self.__current_theme == 'Dark':
            return DarkThemeFactory(self, self.__main, city_list)

        elif self.__current_theme == 'Gray':
            return GrayThemeFactory(self, self.__main, city_list)


    def swap_theme(self, selected_theme) -> None:
        """
        Переключает тему на основе выбранного значения из combobox`s.
        Уничтожает существующие виджеты и создает новые для новой темы.
        :param selected_theme: Текущая выбранная тема.
        :return: None
        """

        for widget in self.__main.winfo_children():
            widget.destroy()

        self.__current_theme = selected_theme

        self.__widgets = self.__create_factory()


    @property
    def widgets(self):
        return self.__widgets