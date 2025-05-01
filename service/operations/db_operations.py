from service.templates.requests_db import *
from tools.load_data import LoadData as ld
from interface.service_db import ADB


class DBOperations(ADB):
    def __init__(self):
        self._create_table()


    def _create_table(self) -> None:
        """
        Создает таблицу погоды в базе данных
        """
        try:
            self._cursor, self._connect = ld.connect(create_table)

        except Exception as e:
            raise RuntimeError(f"Ошибка при создании таблицы: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)


    def add_record(self, *args) -> None:
        """
        Добавляет запись в базу данных
        :param args: параметры для SQL-запроса добавления записи
        """
        try:
            self._cursor, self._connect = ld.connect(add_record, args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Невозможно добавить запись: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)


    def get_records(self):
        """
        Получает все записи из базы данных
        :return: Кортеж записей
        """
        try:
            self._cursor, self._connect = ld.connect(get_record)
            return self._cursor.fetchall()

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении записей: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)


    def update_record(self, *args):
        """
        Очищает таблицу базы данных
        :return: True если успешно
        """
        print(args)
        try:
            self._cursor, self._connect = ld.connect(update_record, args)
            self._connect.commit()

        except Exception as e:
            raise RuntimeError(f"Ошибка при обновлении таблицы: {e}")

        finally:
            self.close_connect(self._cursor, self._connect)



    def close_connect(self, cursor, connect):
        if connect:
            cursor.close()
            connect.close()


