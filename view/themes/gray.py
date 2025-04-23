from view.interface.widget_factory import AWidgetFactory
from config.themes import themes
import customtkinter as ctk




class GrayThemeCreator(AWidgetFactory):

    def __init__(self, controller, main, city_list):
        super().__init__(main)
        self.__city_list: list[str] = city_list
        self.__controller = controller
        self._create_main_frame()
        self._create_exit_button()
        self._create_swap_cbox()
        self._create_title_label()
        self._create_city_weather_label()


    def _create_main_frame(self) -> None:
        self._frame = ctk.CTkFrame(self._main, fg_color='#635959', width=700, height=700)
        self._frame.pack()


    def _create_exit_button(self) -> None:
        self._exit_btn = ctk.CTkButton(self._frame,
                                       text='Close',
                                       text_color='black',
                                       width=200,
                                       height=50,
                                       fg_color='#510973',
                                       font=('Helvetica', 18, 'bold'),
                                       hover_color='#6e1c8a',
                                       command=self._main.on_exit_click)

        self._exit_btn.place(relx=0.35, rely=0.85)


    def _create_swap_cbox(self) -> None:
        self._swap_theme_cbox = ctk.CTkComboBox(self._frame,
                                                text_color='black',
                                                values=themes,
                                                width=120, height=40,
                                                justify='center',
                                                fg_color='gray',
                                                button_color='#510973',
                                                font=('Helvetica', 14, 'bold'),
                                                button_hover_color='#6e1c8a',
                                                border_color='#510973',
                                                dropdown_text_color='black',
                                                dropdown_fg_color='gray',
                                                command=self.__controller.swap_theme)

        self._swap_theme_cbox.set('Gray')
        self._swap_theme_cbox.place(relx=0.8, rely=0.02)


    def _create_title_label(self) -> None:
        self._title = ctk.CTkLabel(self._frame,
                                   width=400,
                                   height=70,
                                   font=('Helvetica', 24, 'bold'),
                                   fg_color="transparent",
                                   justify='center',
                                   text='Weather forecast by city',
                                   text_color='black')

        self._title.place(relx=0.2, rely=0.02)


    def _create_city_weather_label(self):
        pass