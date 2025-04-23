from abc import ABC, abstractmethod
from config.themes import themes
import customtkinter as ctk

class AWidgetFactory(ABC):

    def __init__(self, main):
        self._main = main
        self._frame: ctk.CTkFrame | None = None
        self._label: ctk.CTkLabel | None = None
        self._exit_btn: ctk.CTkButton | None = None
        self._swap_theme_cbox: ctk.CTkComboBox | None = None
        self._create_label()
        self._create_main_frame()
        self._create_exit_button()
        self._create_swap_cbox()


    @abstractmethod
    def _create_main_frame(self) -> None:
        pass


    @abstractmethod
    def _create_exit_button(self, *args, **kwargs) -> None:
        pass


    @abstractmethod
    def _create_swap_cbox(self, *args, **kwargs) -> None:
        pass


    @abstractmethod
    def _create_label(self, *args, **kwargs) -> None:
        pass



class LightFactory(AWidgetFactory):

    def __init__(self, main, city_list):
        super().__init__(main)
        self.__city_list: list[str] = city_list
        self._create_main_frame()
        self._create_exit_button()
        self._create_swap_cbox()
        self._create_label()


    def _create_main_frame(self) -> None:
        self._frame = ctk.CTkFrame(self._main, fg_color='white', width=700, height=700)
        self._frame.pack()

    def _create_exit_button(self) -> None:
        self._exit_btn = ctk.CTkButton(self._frame, text='Close', text_color='black', width=200, height=50, fg_color='#18a5cc', font=('Helvetica', 18, 'bold'), hover_color='#117996', command=self._main.on_exit_click)
        self._exit_btn.place(relx=0.35, rely=0.85)

    def _create_swap_cbox(self) -> None:
        self._swap_theme_cbox = ctk.CTkComboBox(self._frame, text_color='black', fg_color='#a39e9e', values=themes, width=120, height=40, justify='center', button_color='#18a5cc', font=('Helvetica', 14, 'bold'), button_hover_color='#117996', border_color='#18a5cc', dropdown_text_color='black', dropdown_fg_color='#a39e9e', command=self._main.swap_theme)
        self._swap_theme_cbox.place(relx=0.8, rely=0.02)


    def _create_label(self) -> None:
        pass

    @property
    def swap(self) -> str:
        return self._swap_theme_cbox.get()


    @property
    def exit(self) -> ctk.CTkButton:
        return self._exit_btn



class DarkFactory(AWidgetFactory):

    def __init__(self, main, city_list):
        super().__init__(main)
        self.__city_list: list[str] = city_list
        self._create_main_frame()
        self._create_exit_button()
        self._create_swap_cbox()
        self._create_label()

    def _create_main_frame(self) -> None:
        self._frame = ctk.CTkFrame(self._main, fg_color='black', width=700, height=700)
        self._frame.pack()

    def _create_exit_button(self) -> None:
        self._exit_btn = ctk.CTkButton(self._frame, text='Close', text_color='white', width=200, height=50, fg_color='#ad321c', font=('Helvetica', 18, 'bold'), hover_color='#732011', command=self._main.on_exit_click)
        self._exit_btn.place(relx=0.35, rely=0.85)


    def _create_swap_cbox(self) -> None:
        self._swap_theme_cbox = ctk.CTkComboBox(self._frame, text_color='white', values=themes, width=120, height=40, justify='center', button_color='#ad321c', font=('Helvetica', 14, 'bold'), button_hover_color='#732011', border_color='#ad321c', dropdown_text_color='white', dropdown_fg_color='black', command=self._main.swap_theme)
        self._swap_theme_cbox.place(relx=0.8, rely=0.02)



    def _create_label(self) -> None:
        pass

    @property
    def swap(self) -> str:
        return self._swap_theme_cbox.get()


    @property
    def exit(self) -> ctk.CTkButton:
        return self._exit_btn



class GrayFactory(AWidgetFactory):

    def __init__(self, main, city_list):
        super().__init__(main)
        self.__city_list: list[str] = city_list
        self._create_main_frame()
        self._create_exit_button()
        self._create_swap_cbox()
        self._create_label()

    def _create_main_frame(self) -> None:
        self._frame = ctk.CTkFrame(self._main, fg_color='black', width=700, height=700)
        self._frame.pack()

    def _create_exit_button(self) -> None:
        self._exit_btn = ctk.CTkButton(self._frame, text='Close', text_color='white', width=200, height=50, fg_color='#ad321c', font=('Helvetica', 18, 'bold'), hover_color='#732011', command=self._main.on_exit_click)
        self._exit_btn.place(relx=0.35, rely=0.85)


    def _create_swap_cbox(self) -> None:
        self._swap_theme_cbox = ctk.CTkComboBox(self._frame, text_color='white', values=themes, width=120, height=40, justify='center', button_color='#ad321c', font=('Helvetica', 14, 'bold'), button_hover_color='#732011', border_color='#ad321c', dropdown_text_color='white', dropdown_fg_color='black', command=self._main.swap_theme)
        self._swap_theme_cbox.place(relx=0.8, rely=0.02)



    def _create_label(self) -> None:
        pass

    @property
    def swap(self) -> str:
        return self._swap_theme_cbox.get()


    @property
    def exit(self) -> ctk.CTkButton:
        return self._exit_btn