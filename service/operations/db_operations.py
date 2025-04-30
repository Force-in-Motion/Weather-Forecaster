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
            ld.connect(create_table)
        except Exception as e:
            raise RuntimeError(f"Ошибка при создании таблицы: {e}")


    def add_record(self, *args) -> None:
        """
        Добавляет запись в базу данных
        :param args: параметры для SQL-запроса добавления записи
        """
        try:
            ld.connect(add_record, args)
        except Exception as e:
            raise RuntimeError(f"Невозможно добавить запись: {e}")


    def get_records(self) -> tuple[tuple[str]]:
        """
        Получает все записи из базы данных
        :return: Кортеж записей
        """
        try:
            cursor = ld.connect(get_record)
            return cursor.fetchall()
        except Exception as e:
            raise RuntimeError(f"Ошибка при получении записей: {e}")


    def delete_records(self) -> bool:
        """
        Очищает таблицу базы данных
        :return: True если успешно
        """
        try:
            ld.connect(clear_table)
            return True
        except Exception as e:
            raise RuntimeError(f"Ошибка при очистке таблицы: {e}")


