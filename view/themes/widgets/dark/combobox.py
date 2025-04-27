import customtkinter as ctk
from config.themes import themes


class SwapCbox(ctk.CTkComboBox):
    def __init__(self, main, controller):
        super().__init__(main,
                         text_color='#a7a5a8',
                         values=themes,
                         fg_color='black',
                         width=120,
                         height=40,
                         justify='center',
                         button_color='#ad321c',
                         font=('Helvetica', 14, 'bold'),
                         button_hover_color='#732011',
                         border_color='#ad321c',
                         dropdown_text_color='#a7a5a8',
                         dropdown_fg_color='black',
                         command=controller.swap_theme)

        self.set('Dark')
        self.place(relx=0.8, rely=0.02)