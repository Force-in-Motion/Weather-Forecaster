import customtkinter as ctk



class UpdateButton(ctk.CTkButton):
    def __init__(self, main):
        super().__init__(main,
                         text='Close',
                         text_color='#a7a5a8',
                         width=200,
                         height=50,
                         fg_color='#ad321c',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#732011'
                         )

        self.place(relx=0.55, rely=0.85)


class ExitButton(ctk.CTkButton):
    def __init__(self, main_frame, main):
        super().__init__(main_frame,
                         text='Close',
                         text_color='#a7a5a8',
                         width=200,
                         height=50,
                         fg_color='#ad321c',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#732011',
                         command=main.on_exit_click)

        self.place(relx=0.2, rely=0.85)
