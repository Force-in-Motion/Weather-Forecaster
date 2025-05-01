import customtkinter as ctk



class TitleLabel(ctk.CTkLabel):

    def __init__(self, main):
        super().__init__(main,
                         width=400,
                         height=60,
                         font=('Helvetica', 24, 'bold'),
                         fg_color="transparent",
                         justify='center',
                         text='Weather forecast by city',
                         text_color='black')

        self.place(relx=0.2, rely=0.01)



class WeatherSubscriber(ctk.CTkLabel):

    def __init__(self, main, publisher):
        super().__init__(main, text_color='black', anchor='w', font=('Helvetica', 14, 'bold'))
        self.pack(fill='x', padx=10, pady=7)
        self.__main = main
        self.__publisher = publisher
        self.__subscribe()

    def unsubscribe(self) -> None:
        self.__publisher.remove_subscriber(self)

    def __subscribe(self) -> None:
        self.__publisher.add_subscriber(self)


    def update_data(self, weather_object) -> None:
#        print(weather_object.city, weather_object.current_temp, weather_object.wind_speed, weather_object.humidity, weather_object.pressure)
        self.configure(text=f'{weather_object.city}  Температура: {weather_object.current_temp} '
                            f'     Ветер: {weather_object.wind_speed} '
                            f'     Влажность: {weather_object.humidity} '
                            f'     Давление: {weather_object.pressure}')


