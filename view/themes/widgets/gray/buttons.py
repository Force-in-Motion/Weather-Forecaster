import customtkinter as ctk



class UpdateButton(ctk.CTkButton):

    def __init__(self, main):
        super().__init__(main,
                         text='Update',
                         text_color='black',
                         width=200,
                         height=50,
                         fg_color='#662f80',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#6e1c8a')

        self.place(relx=0.55, rely=0.85)


class ExitButton(ctk.CTkButton):

    def __init__(self, main_frame, main):
        super().__init__(main_frame,
                         text='Close',
                         text_color='black',
                         width=200,
                         height=50,
                         fg_color='#662f80',
                         font=('Helvetica', 18, 'bold'),
                         hover_color='#6e1c8a',
                         command=main.on_exit_click)

        self.place(relx=0.2, rely=0.85)
