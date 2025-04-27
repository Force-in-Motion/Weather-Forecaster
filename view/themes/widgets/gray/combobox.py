import customtkinter as ctk
from config.themes import themes


class SwapCbox(ctk.CTkComboBox):
    def __init__(self, main, controller):
        super().__init__(main,
                         text_color='black',
                         values=themes,
                         width=120, height=40,
                         justify='center',
                         fg_color='#787575',
                         button_color='#662f80',
                         font=('Helvetica', 14, 'bold'),
                         button_hover_color='#6e1c8a',
                         border_color='#662f80',
                         dropdown_text_color='black',
                         dropdown_fg_color='#787575',
                         command=controller.swap_theme)

        self.set('Gray')
        self.place(relx=0.8, rely=0.02)