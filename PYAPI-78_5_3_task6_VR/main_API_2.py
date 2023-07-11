### =====
### C:\Users\Romanov\Documents\000_MyDocs\00_doc_VR1_psw111\Netology_VR3\5_OOP_API_Repo\5_OOP_API_RPZ\PYAPI-78_5_3_task6_VR\main_API_2.py
### =====

import json
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        name_file = path_to_file.split('\\')[-1]
        params = {'path': f'{name_file}'}
        headers = {'Authorization': token}

        response = requests.get(url, headers=headers, params=params)

        url_for_upload = response.json().get('href', '')
        with open('7_1_vrangel.jpg', 'rb') as file:
            response2 = requests.put(url_for_upload, files={"file": file})

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r'C:\Users\apomelov\Desktop\TEST\Homework_file\API\7_1_vrangel.jpg'
    token = 'OAuth '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)