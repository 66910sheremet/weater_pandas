from logic import Processing
# import pprint
# from datetime import datetime

# import matplotlib.pyplot as plt

r"C:\Users\Eugene\Downloads\data1.xls"

work = Processing()
work.preliminary_processing()
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


