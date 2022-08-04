import pandas as pd
import matplotlib.pyplot as plt


"""
Step 1:
Программа для чтения csv/xls файла:
Функция ввода ссылки на файл                                                       done
Первый столбец (индекс) - дата в формате "дд.мм.гггг чч:мм"                        done
Второй столбец - температура за определенный час.                                  done

Что нужно реализовать: 
1.1 Первая колонка в виде датафрейма                                               done
1.2 Избавиться от часов                                                            done
1.3 Вычислить средниесуточные                                                      done
1.4 Начальная и конечные даты рассматриваемого периода                             done                             
1.5. Проанализировать сколько пропущенных ячеек(дней)!                             done
1.6. Вывести даты без значений                                                     
2. Заполнить пропущенные ячейки средним значением за день
(или посчитать среднее значение за день без учета пропущенных значений)
3. Сгруппировать по дням со среденей темпераутрой за день.                         done
4.1 Разбить наблюдения по годам. 
4.2. Визуализация температур, например, за конкретный год.
"""
r"C:\Users\Eugene\Downloads\data1.xls"

#link = input("Введите ссылку на интересующий файл:")
data = pd.read_excel(r"C:\Users\Eugene\Downloads\data1.xls")                                                             # открываем файл на чтение
T2005_2022 = data[["data","T"]]                                                                                          # забираем 2 колонки с датой и температурой
test2005_2022 = T2005_2022                                                                                               # пока что тестировочный файлик
test2005_2022["data"] = pd.to_datetime(test2005_2022["data"], format="%d.%m.%Y %H:%M").dt.date                           # приводим столбец с датами в формат dataframe и сразу удаляем часы и минуты
T_meanday = test2005_2022.groupby("data").agg({"T":"mean"})                                                              # считаем среднюю температуру по дням / автоматическая сортировка по дате с ранней
#print(test2005_2022.head())

start_chain = T_meanday.index[0]                                                                                         # начальная дата исследуемого периода
end_chain = T_meanday.index[-1]                                                                                          # конечная дата исследуемого периода
start_chain_with_desc = f"Начальная дата исследуемого периода: {T_meanday.index[0]}"
end_chain_with_desc = f"Конечная дата исследуемого периода: {T_meanday.index[-1]}"
days_with_temp = (end_chain - start_chain)                                                                               # количество дней между начальной и конечной датами
days_with_temp_with_desc = f"Количество дней между начальной и конечной датами: {days_with_temp.days} дней"
total_cols = len(T_meanday)                                                                                              # фактическое количество дней с данными по температуре
total_cols_with_desc = f"Фактическое количество дней с данными по температуре: {total_cols} дней"
numbers_of_missing_days = ((end_chain - start_chain).days) - len(T_meanday)                                              # количество пропущенных дней временной последовательности
numbers_of_missing_days_with_desc = f"Количество пропущенных дней временной последовательности " \
                                    f"{numbers_of_missing_days}"

t = T_meanday["T"].values.tolist()
T_meanday["dates"] = T_meanday.index

list_of_dates = T_meanday["dates"].astype(str).tolist()
list_of_dates = set(list_of_dates)
#print(t)                                                                                     # проверка что все значения в индексе одинаковые
#print(list_of_dates)
print(list_of_dates)


#print(T_meanday.head())                временно закоментить
#print(start_chain_with_desc)
#print(end_chain_with_desc)
#print(days_with_temp_with_desc)
#print(total_cols_with_desc)
#print(numbers_of_missing_days_with_desc)

#test2005_2022.sort_index(inplace=True)
#print(test2005_2022.index[-1])
#print(test2005_2022.head())
#T_meanday.head().plot(kind = "bar", subplots = False, sharex = False, figsize=(40, 20))
#plt.show()
