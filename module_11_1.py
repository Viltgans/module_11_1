from pprint import pprint
import pandas as pd

# Создаем базу данных псевдо-csv
df = pd.DataFrame([[1,'Bob', 'Builder', 33],
                  [2,'Sally', 'Baker', 28],
                  [3,'Scott', 'Maker', 27]],
columns=['id','name', 'occupation', 'age'])

# Создаем вторую базу данных псевдо-csv
new_df = pd.DataFrame([[4, 'Alex', 'Giver', 55],
                       [5, 'Sally', 'Taker', 13]],
columns=['id','name', 'occupation', 'age'])

# Соединяем две базы данных
try_df = pd.concat([df, new_df], ignore_index=True)

# Записываем данные в csv файл
try_df.to_csv('data.csv', index=False)
# Считываем данные из csv файла
data = pd.read_csv('data.csv')

# Сортируем базу данных ТОЛЬКО по имени в алфавитном порядке,
# при значении ascending=False алфавитный порядок будет инверсирован.
sort_df = data.sort_values('name', ascending=True)
print(sort_df, '\n')

# Выводим информацию о базе, verbose=True выводит информацию по всем столбцам.
# .info(memory_usage='deep') - позволяет получить более точные данные по используемой памяти.
information = sort_df.info(verbose=False, memory_usage='deep')
print(information, '\n')

# Сортирует по dtype: exclude - все исключая указанный; include - только тот, который указали.
another_sort_df = sort_df.select_dtypes(exclude=['int64'])
print(another_sort_df, '\n')

# Получаем размер в виде умноженных строк на столбцы
size_df = sort_df.size
print(size_df, '\n')
#
# Выводим первые 2 строки данных. Если не передать значение выведется первые 5 строк.
print(data.head(2), '\n')
# Например, подсчитаем количество уникальных значений в столбце 'name'
unique_values = sort_df['name'].nunique()
print(f'Количество уникальных значений в столбце "name": {unique_values}')

# Например, можно вывести среднее значение по столбцу 'age'
mean_value = sort_df['age'].mean()
print(f'Среднее значение по столбцу "age": {mean_value}')
