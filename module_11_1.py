import requests
import pandas as pd
import numpy as np

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Возврат данных в формате JSON
    else:
        return f"Ошибка: {response.status_code}"
# Пример использования
# data = get_data('https://api.example.com/data')
# print(data)

def post_data(url, payload):
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        return response.json()  # Возврат данных в формате JSON
    else:
        return f"Ошибка: {response.status_code}"
# Пример использования
# payload = {'key': 'value'}
# response_data = post_data('https://api.example.com/submit', payload)
# print(response_data)

def get_response_headers(url):
    response = requests.head(url)
    return response.headers  # Возврат заголовков ответа
# Пример использования
# headers = get_response_headers('https://api.example.com/')
# print(headers)

############################################################################

def read_csv(file_path, n=5):
    df = pd.read_csv(file_path)
    return df.head(n)
#Чтение CSV файла и вывод первых N строк:

def filter_by_column(df, column_name, value):
    return df[df[column_name] == value]
#Фильтрация DataFrame по значению в столбце

def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)
#Сохранение DataFrame в новый CSV файл

df = read_csv('data.csv')
filtered_df = filter_by_column(df, 'column_name', 'value')
save_to_csv(filtered_df, 'filtered_data.csv')

############################################################################

def create_array(values):
    return np.array(values)

def calculate_mean(arr):
    return np.mean(arr)

def calculate_sum(arr):
    return np.sum(arr)

arr = create_array([1, 2, 3, 4, 5])
mean_value = calculate_mean(arr)
total_sum = calculate_sum(arr)

print("Среднее значение:", mean_value)
print("Сумма элементов:", total_sum)