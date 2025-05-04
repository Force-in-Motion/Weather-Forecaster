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
                         fg_color='#454343',
                         border_color='#643687',
                         button_color='#643687',
                         dropdown_text_color='black',
                         dropdown_fg_color='#454343',
                         button_hover_color='#532c70',
                         font=('Helvetica', 14, 'bold'),
                         command=controller.swap_theme)

        self.set('gray')
        self.place(relx=0.8, rely=0.02)