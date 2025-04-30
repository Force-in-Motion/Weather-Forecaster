import json
import os
import sqlite3


class LoadData:

    @staticmethod
    def get_token_path() -> str:
        """
        Создает относительный путь к файлу common_areas
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path_token = os.path.join(current_dir, '..', 'config', 'token', 'weather_api.json')

        return os.path.abspath(path_token)



    @staticmethod
    def get_db_path() -> str:
        """
        Создает относительный путь к файлу common_areas
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        path_db = os.path.join(current_dir, '..', 'storage', 'database.db')

        return os.path.abspath(path_db)


    @staticmethod
    def del_file(path) -> None:
        """
        Удаляет файл по полученному пути
        :param path: Принимает путь
        :return: None
        """
        if os.path.exists(path):
            os.remove(path)


    @staticmethod
    def get_token() -> str:
        """
        Получает токен по указанному пути
        :return: Токен в виде строки
        """
        with open(LoadData.get_token_path(), 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['api_key']


    @staticmethod
    def connect(query: str, params: tuple = ()):
        """
        Выполняет SQL-запрос с параметрами (если есть) и возвращает курсор.

        :param query: SQL-запрос в виде строки
        :param params: кортеж параметров для запроса (по умолчанию пустой)
        :return: sqlite3.Cursor
        """
        db_path = LoadData.get_db_path()

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor