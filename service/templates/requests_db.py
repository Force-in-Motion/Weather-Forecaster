create_table =  """
                CREATE TABLE IF NOT EXISTS CityWeather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
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


clear_table = """ DELETE FROM CityWeather"""