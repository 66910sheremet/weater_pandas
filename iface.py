from logic import Processing
# import pprint
# from datetime import datetime

# import matplotlib.pyplot as plt

r"C:\Users\Eugene\Downloads\data1.xls"

work = Processing()
while True:
    link_input = input("Введите ссылку на интересующий файл:")
    if link_input.endswith('.xls'):
        work.preliminary_processing_excel(link_input)
        print("Для сохрания датасета с усредненной температурой, введите 1")
        print("Для сохранения датасета из дат без данных, введите 2")
        print("Для дальнейшей обработки введите 3")
        print("Для вывода списка со среднемесячными температурами введите 4")
        print("Для обработки конкретного отопительного периода нижмите 5")
        choice = input("Enter your choice:")
        if choice == "1":
            work.save_dataset_mean_temp()
        elif choice == "4":
            work.get_average_monthly_temperature()
            print("Сохранить датасет со среднемесячными температурами: Y/N")
            choice_save_ma = input("Enter your choice:")
            if choice_save_ma == "Y":
                work.save_dataset_average_monthly_temperature()
            elif choice_save_ma == "N":
                print("New operations")
        elif choice == "5":
            work.heating_period_treatment()
            # print("Для сохранения датасета реального отопительного периода, нажмите 1")
            # ch_ds_hp = input("Enter your choice:")
            # if ch_ds_hp == '1':
            #    work.save_ds_duration_heating_period()
    elif link_input.endswith('.csv'):
        work.preliminary_processing_csv(link_input)
        print("Для сохрания датасета с усредненной температурой, введите 1")
        print("Для сохранения датасета из дат без данных, введите 2")
        print("Для дальнейшей обработки введите 3")
        print("Для вывода списка со среднемесячными температурами введите 4")
        print("Для обработки конкретного отопительного периода нижмите 5")
        choice = input("Enter your choice:")
        if choice == "1":
            work.save_dataset_mean_temp()
        elif choice == "4":
            work.get_average_monthly_temperature()
            print("Сохранить датасет со среднемесячными температурами: Y/N")
            choice_save_ma = input("Enter your choice:")
            if choice_save_ma == "Y":
                work.save_dataset_average_monthly_temperature()
            elif choice_save_ma == "N":
                print("New operations")
        elif choice == "5":
            work.heating_period_treatment()
            # print("Для сохранения датасета реального отопительного периода, нажмите 1")
            # ch_ds_hp = input("Enter your choice:")
            # if ch_ds_hp == '1':
            #    work.save_ds_duration_heating_period()
    else:
        print(r'Введите ссылку в формате C:\Users\Eugene\Downloads\data1.xls или ..\data1.csv')



