import math
from utils import gost_table  # Импортируем модуль для получения данных из таблиц
from utils import gost_table_gost

def calculate_volume(diameter_cm, length_m, log_quantity=1, method="ISO 4480-83"):
    """
    Вычисляет объем древесины по заданному методу.
    
    Обязательные параметры:
      diameter_cm - диаметр в сантиметрах
      length_m    - длина в метрах
      
    Опциональные параметры:
      log_quantity - количество бревен (по умолчанию 1)
      method       - метод расчета (по умолчанию "ISO 4480-83")
      
    Возвращает:
      volume       - базовый объем для одного элемента
      unit         - единица измерения ("m3" или "BF")
      total_volume - объем с учетом количества (volume * log_quantity)
    """
    # Конвертация
    diameter_m_val = float(diameter_cm) / 100.0
    diameter_inch = float(diameter_cm) / 2.54

    if method == "ISO 4480-83":
        # Находим ближайший доступный набор в таблице по значению длины
        available_grades = list(gost_table.ISO_4480_83_TABLE.keys())
        table_grade = min(available_grades, key=lambda k: abs(k - float(length_m)))
        volume = gost_table.get_volume(float(diameter_cm), float(length_m), table_grade=table_grade)
        unit = "m3"
    elif method == "International 1/4 Log Rule":
        volume = ((diameter_inch - 1) ** 2 * float(length_m)) / 16
        unit = "BF"
        print(f"calculate_volume вызвана: method={method}, diameter_cm={diameter_cm}, length_m={length_m}")
    elif method == "Doyle Log Rule":
        print(f"Doyle: diameter_inch={diameter_inch}, length_m={length_m}")
        if diameter_inch > 4:
            volume = ((diameter_inch - 4) ** 2 * float(length_m)) / 16
        else:
            volume = 0  # Ошибка ввода
        unit = "BF"
    elif method == "Scribner Log Rule":
        print(f"Scribner: diameter_inch={diameter_inch}, length_m={length_m}")
        if diameter_inch > 0:
            volume = (0.79 * (diameter_inch ** 2) - 2 * diameter_inch - 4) * float(length_m) / 12
        else:
            volume = 0
        unit = "BF"
    elif method == "JAS Scale":
        volume = 0.7854 * ((diameter_m_val - 0.013) ** 2) * float(length_m)
        unit = "m3"
    elif method == "Hoppus Log Rule":
        volume = (diameter_inch ** 2) / 144 * float(length_m) * 2.83
        unit = "BF"
    elif method.upper() in ["GOST 2708-75", "ГОСТ 2708-75"]:
        # Выбираем набор коэффициентов согласно длине
        available_grades = list(gost_table_gost.GOST_2708_75_TABLE.keys())
        table_grade = min(available_grades, key=lambda k: abs(k - float(length_m)))
        volume = gost_table_gost.get_volume_gost2708(float(diameter_cm), float(length_m), table_grade=table_grade)
        unit = "m3"   # Добавлено присвоение единицы измерения    
    else:
        raise ValueError("Неизвестный метод")
    
    total_volume = volume * float(log_quantity)
    return volume, unit, total_volume