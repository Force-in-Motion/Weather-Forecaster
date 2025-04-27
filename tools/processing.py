class ProcessingData:

    @staticmethod
    def converts_to_bars(pressure_mb):
        return pressure_mb / 1000

    @staticmethod
    def converts_wind_speed_in_mps(wind_speed_kph):
        return wind_speed_kph * 0.27778