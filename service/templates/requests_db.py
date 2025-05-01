create_table =  """
                CREATE TABLE IF NOT EXISTS CityWeather (
                    city TEXT UNIQUE,
                    temperature REAL,
                    humidity REAL,
                    pressure REAL,
                    wind_speed REAL
                    )
                """


add_record =   """
                INSERT INTO CityWeather (city, temperature, humidity, pressure, wind_speed)
                    VALUES (?, ?, ?, ?, ?)
                """


get_record = """ SELECT * FROM CityWeather """


update_record = """ UPDATE CityWeather SET temperature = ?, humidity = ?, pressure = ?, wind_speed = ? WHERE city = ? """
