import customtkinter as ctk
from src.config.themes import themes


class SwapCbox(ctk.CTkComboBox):
    """ Формирует объект Combobox, содержащий названия тем для их смены """

    def __init__(self, main, controller):
        super().__init__(main,
                         width=120,
                         height=40,
                         values=themes,
                         justify='center',
                         text_color='black',
                         fg_color='#a39e9e',
                         border_color='#18a5cc',
                         button_color='#1d87b5',
                         dropdown_text_color='black',
                         dropdown_fg_color='#a39e9e',
                         button_hover_color='#117996',
                         font=('Helvetica', 14, 'bold'),
                         command=controller.swap_theme)

        self.set('light')
        self.place(relx=0.8, rely=0.02)