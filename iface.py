from logic import Processing
#import pprint
#from datetime import datetime

import matplotlib.pyplot as plt

r"C:\Users\Eugene\Downloads\data1.xls"

work = Processing()
work.preliminary_processing()
print("Для сохрания датасета с усредненной температурой, введите 1")
print("Для сохранения датасета из дат без данных, введите 2")
print("Для дальнейшей обработки введите 3")
choice = input("Enter your choice:")
if choice == "1":
    work.save_dataset_mean_temp()
