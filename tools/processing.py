class ProcessingData:

    @staticmethod
    def converts_pressure_in_mm_hg(pressure_mb) -> float:
        """
        Конвертирует давление из милли баров в миллиметры ртутного столба и округляет до 2 знаков после запятой
        :param pressure_mb:давление в милли барах
        :return:
        """
        return round(pressure_mb * 0.750062, 2)

    @staticmethod
    def converts_wind_speed_in_mps(wind_speed_kph) -> float:
        """
        Конвертирует полученной значение скорости ветра из км/час в привычное м/секунду и округляет до 2 знаков после запятой
        :param wind_speed_kph: скорость ветра в км/час
        :return:
        """
        return round(wind_speed_kph * 0.27778, 2)