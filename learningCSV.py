import pandas as pd

# df = pd.read_csv('/Users/viktortarkhanov/Desktop/pythonCourses/seminars/filesCSVforSeminar9/california_housing_train.csv')

# head = df.head(10) # вывод шапки (первых 10 строк)
# print(head)

# tail = df.tail(5) # вывод хвоста (последние 5 строк)
# print(tail)

# print(df.shape) # вывод количества столбцов и строк

# print(df.isnull().sum()) # показывает сколько под ключом(столбцом) ячеек пустых

# # Проверить тип данных в столбцах
# # В данных случаях везде float, число 64 указывает на разрядность(Используется 64 байта для хранения значения в памяти,
# # чем меньше разрядность, тем меньший диапазон могут принимать числа и тем меньше тратится памяти на хранение.
# print(df.dtypes)

# # Посмотреть все столбцы
# # Возвращает список со строками строк - названиями столбцов в таблице
# print(df.columns)

#task01
print('\tЗадание 1')
df = pd.read_csv('/Users/viktortarkhanov/Desktop/pythonCourses/seminars/filesCSVforSeminar9/california_housing_test.csv')
print(f'\tКоличество строк, столбцов: \n{df.shape}')

print(f'\tТипы данных в столбцах: \n{df.dtypes}')

print(f'\tКоличество пустых ячеек в столбцах: \n{df.isnull().sum()}')

# Data Choices (выборки данных из таблицы)
# Выбор 1 столбца - [широты]
# print(df['latitude']) 

# # Выбор нескольких столбцов [широта, кол-во жителей]
# print(df[['latitude', 'population']])

# # Выбор определенного кол-ва рядов
# # Синтаксис df[df[col] !=|==|>|<| значение]
# print(df[df['housing_median_age'] < 30])

# # Для отбора можно использовать несколько условий одновременно
# # Знак & означает 'and', а знак | 'or'
# print(df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)])
# print(df[(df['housing_median_age'] > 20) | (df['total_rooms'] > 2000)])

# # Выбор определенного кол-ва рядов и столбцов
# # используется метод loc в [], первый аргумент индекс или селектор, а второй список со столбцами
# x=df.loc[df['population'] < 100, ['total_bedrooms', 'total_rooms']]
# print(x)

#task2
print('\tЗадание 2')
print(df.loc[df['median_income'] < 2, ['median_house_value']])

print(df.columns)

print(df[['longitude', 'latitude']])

print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])

# simple statistic
# Pandas позволяет получить основные простые данные для описательной статистики
# Такие как минимальное значение в столбце, максимальное значение, сумма всех значений, среднее значение

# Максимальное значение
# print(df['population'].max())
# # Минимальное значение
# print(df['population'].min())
# # Среднее значение
# print(df['population'].mean())
# # Сумма
# print(df['population'].sum())

# # Медианное значение
# print(df[['population', 'total_rooms']].median())

# print(df.describe())

# count - Общее кол-во не пустых строк
# mean - среднее значение в столбце
# std - стандартное отклонение от среднего значения
# min - минимальное значение
# max - максимальное значение
# Числа 25%, 50%, 75% - перцентили
# Перцентиль - это показатель, используемый в статистике, показывающий значение, ниже 
# которого падает определенный процент наблюдений в группе наблюдений

#task3
print('\tЗадание 3')
print(f'Минимальное значение в median_house_value: {df['median_house_value'].min()}')
print(f'Максимальное значение в median_house_value: {df['median_house_value'].max()}')
print(f'Значения столбца Median_house_value при значении median_income = 3.1250: \n{df.loc[df['median_income'] == 3.1250, ['median_house_value']]}')
