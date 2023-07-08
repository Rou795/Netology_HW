import json

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_list: list):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        if not(file_list):
            return f'Список файлов пуст, загружать нечего.'
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = {'Authorization': self.token}
        for name in file_list:
            param = {'path': '/' + name.strip(' ')}
            response = requests.get(url, headers=headers, params=param)
            if 200 <= response.status_code < 300:
                data = response.json()
                url_up = data['href']
                with open(name.strip(' '), 'rb') as f:
                    response = requests.post(url_up, files={'file': f})
                    if 200 <= response.status_code < 300:
                        print(f'Файл {name.strip(" ")} успешно загружен на диск.')
                    elif response.status_code >= 500:
                        print(f'Ошибка на сервере Диска. Файл {name.strip(" ")} не загружен.')
                    elif 400 <= response.status_code < 500:
                        print(f'Ошибка в работе программы. Файл {name.strip(" ")} не загружен.')
            elif response.status_code == 401:
                print(f'Ошибка в токене. Файл {name.strip(" ")} не загружен.')
            elif response.status_code >= 500:
                print(f'Ошибка на сервере Диска. Файл {name.strip(" ")} не загружен.')
            elif 400 <= response.status_code < 500:
                print(f'Ошибка в работе программы. Файл {name.strip(" ")} не загружен.')


if __name__ == '__main__':
    # Получаем пути к файлам и токен от пользователя. При этом корректируем данные, чтобы избавиться
    # от возможных неточностей при получении текста
    files = input(f'Введите пути к файлам, которые требуется загрузить на яндекс диск через запятую: ')
    file_list_in = files.split(',')
    token_in = input(f'Введите токен для закгрузки файлов на яндекс диск: ')
    user = YaUploader(token_in.strip(' '))
    user.upload(file_list_in)
