from abc import ABC, abstractmethod
import customtkinter as ctk

class AWidgetFactory(ABC):

    def __init__(self, main):
        self._main = main
        self._frame: ctk.CTkFrame | None = None
        self._label: ctk.CTkLabel | None = None
        self._exit_btn: ctk.CTkButton | None = None
        self._swap_theme_cbox: ctk.CTkComboBox | None = None


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