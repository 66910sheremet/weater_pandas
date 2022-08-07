import pandas as pd
import pprint
from datetime import datetime
import matplotlib.pyplot as plt

#C:\Users\Eugene\Downloads\data1.xls пример ссылки


class Processing:

    def preliminary_processing():
        #link = input("Введите ссылку на интересующий файл:")
        link_input = input("Введите ссылку на интересующий файл:")
        link = link_input.replace("\\","/")
        data = pd.read_excel(link)                                                                                          # открываем файл на чтение
        T2005_2022 = data[["data","T"]]                                                                                     # забираем 2 колонки с датой и температурой
        test2005_2022 = T2005_2022                                                                                          # пока что тестировочный файлик
        test2005_2022["data"] = pd.to_datetime(test2005_2022["data"], format="%d.%m.%Y %H:%M").dt.date                      # приводим столбец с датами в формат dataframe и сразу удаляем часы и минуты
        T_meanday = test2005_2022.groupby("data").agg({"T":"mean"})                                                         # считаем среднюю температуру по дням / автоматическая сортировка по дате с ранней
        #print(test2005_2022.head())

        start_chain = T_meanday.index[0]                                                                                    # начальная дата исследуемого периода
        end_chain = T_meanday.index[-1]                                                                                     # конечная дата исследуемого периода
        start_chain_with_desc = f"Начальная дата исследуемого периода: {T_meanday.index[0]}"
        end_chain_with_desc = f"Конечная дата исследуемого периода: {T_meanday.index[-1]}"
        days_with_temp = (end_chain - start_chain)                                                                          # количество дней между начальной и конечной датами
        days_with_temp_with_desc = f"Количество дней между начальной и конечной датами: {days_with_temp.days} дней"
        total_cols = len(T_meanday)                                                                                         # фактическое количество дней с данными по температуре
        total_cols_with_desc = f"Фактическое количество дней с данными по температуре: {total_cols} дней"
        numbers_of_missing_days = ((end_chain - start_chain).days) - len(T_meanday)                                         # количество пропущенных дней временной последовательности
        numbers_of_missing_days_with_desc = f"Количество пропущенных дней временной последовательности " \
                                        f"{numbers_of_missing_days}"

        #t = T_meanday["T"].values.tolist() лист со значениями температуры (пока не нужен)
        T_meanday["dates"] = T_meanday.index

        list_of_dates = set(T_meanday["dates"].astype(str).tolist())                                                        # создали множество с датами с температурой
        fact_list_of_dates = set(pd.date_range(start=start_chain, end=end_chain).astype(str))
        missing_dates = list(fact_list_of_dates - list_of_dates)
        missing_dates = pd.DatetimeIndex(missing_dates).sort_values()

        list_of_missing_dates = list(missing_dates.astype(str).tolist())                                                    # список с датами для которых нет измерений температуры
        lenth_of_list_of_missing_dates = len(list_of_missing_dates)
        #list_of_missing_dates = missing_dates.values.tolist()
        T_meanday.drop(columns="dates", inplace=True)                                                                       # удаляем уже ненужный столбец  с датами
        #print(fact_list_of_dates)
        #list_of_dates = set(list_of_dates)
        #print(T_meanday.head())                                                                                            # проверка что все значения в индексе одинаковые
        #print(list_of_dates)
        #print(list_of_dates)


        #print(T_meanday.head())
        print(start_chain_with_desc)
        print(end_chain_with_desc)
        print(days_with_temp_with_desc)
        print(total_cols_with_desc)
        print(numbers_of_missing_days_with_desc)

        #test2005_2022.sort_index(inplace=True)
        #print(test2005_2022.index[-1])
        #print(test2005_2022.head())
        print(f"Количество дней с пропущенными данными: {lenth_of_list_of_missing_dates}")
        pprint.pprint(f"Список дат с отсутствующими данными по температуре: {list_of_missing_dates}")
        #T_meanday.head().plot(kind = "bar", subplots = False, sharex = False, figsize=(40, 20))
        #plt.show()