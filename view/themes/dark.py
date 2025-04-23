from view.interface.widget_factory import AWidgetFactory
from config.themes import themes
import customtkinter as ctk




class DarkThemeCreator(AWidgetFactory):

    def __init__(self, controller, main, city_list):
        super().__init__(main)
        self.__city_list: list[str] = city_list
        self.__controller = controller
        self._create_main_frame()
        self._create_exit_button()
        self._create_swap_cbox()
        self._create_label()


    def _create_main_frame(self) -> None:
        self._frame = ctk.CTkFrame(self._main, fg_color='black', width=700, height=700)
        self._frame.pack()


    def _create_exit_button(self) -> None:
        self._exit_btn = ctk.CTkButton(self._frame,
                                       text='Close',
                                       text_color='white',
                                       width=200,
                                       height=50,
                                       fg_color='#ad321c',
                                       font=('Helvetica', 18, 'bold'),
                                       hover_color='#732011',
                                       command=self._main.on_exit_click)

        self._exit_btn.place(relx=0.35, rely=0.85)


    def _create_swap_cbox(self) -> None:
        self._swap_theme_cbox = ctk.CTkComboBox(self._frame,
                                                text_color='white',
                                                values=themes,
                                                fg_color='black',
                                                width=120,
                                                height=40,
                                                justify='center',
                                                button_color='#ad321c',
                                                font=('Helvetica', 14, 'bold'),
                                                button_hover_color='#732011',
                                                border_color='#ad321c',
                                                dropdown_text_color='white',
                                                dropdown_fg_color='black',
                                                command=self.__controller.swap_theme)

        self._swap_theme_cbox.set('Dark')
        self._swap_theme_cbox.place(relx=0.8, rely=0.02)



    def _create_label(self) -> None:
        pass
