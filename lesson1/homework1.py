print("""
Домашнее задание 1
Дисциплина: Наука о данных для юристов
Тема: Введение в Python
""")

# =====================================================
# ЗАДАНИЕ 1: Работа с переменными, ввод/вывод, id()
# =====================================================

print("=" * 50)
print("ЗАДАНИЕ 1")
print("=" * 50)

# Создаём переменные разных типов
student_name = "Иван Петров"
student_age = 20
student_grade = 4.8
is_attending = True

# Выводим переменные на экран
print("--- Созданные переменные ---")
print("Имя студента:", student_name)
print("Возраст:", student_age)
print("Средний балл:", student_grade)
print("Посещает занятия:", is_attending)
print()

# Запрашиваем данные у пользователя
print("--- Ввод данных от пользователя ---")
user_name = input("Введите ваше имя: ")
user_age = input("Введите ваш возраст: ")
user_hobby = input("Введите ваше хобби: ")

# Выводим введённые данные
print("\n--- Вывод введённых данных ---")
print("Вас зовут:", user_name)
print("Ваш возраст:", user_age)
print("Ваше хобби:", user_hobby)
print()

# Наблюдение за id() — изменяемые и неизменяемые объекты
print("--- Наблюдение за id() ---")

# Неизменяемый объект (int, str, float и др.)
print("Пример с неизменяемым объектом (int):")
number = 100
print("number =", number, "| id =", id(number))
number = number + 50
print("number =", number, "| id =", id(number), "- ИЗМЕНИЛСЯ!")
print()

# Изменяемый объект (list, dict, set и др.)
print("Пример с изменяемым объектом (list):")
my_list = [1, 2, 3]
print("my_list =", my_list, "| id =", id(my_list))
my_list.append(4)
print("my_list =", my_list, "| id =", id(my_list), "- ОСТАЛСЯ ТЕМ ЖЕ!")
print()

input("\nНажмите Enter для перехода к заданию 2...")
print("\n" * 2)


# =====================================================
# ЗАДАНИЕ 2: Перевод секунд в часы, минуты, секунды
# =====================================================

print("=" * 50)
print("ЗАДАНИЕ 2")
print("=" * 50)

def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

# Запрашиваем время в секундах
seconds_input = input("Введите время в секундах: ")

# Проверяем, что введены только цифры (метод .isdigit())
if seconds_input.isdigit():
    total_seconds = int(seconds_input)  # преобразуем строку в число
    
    # Используем функцию для расчёта
    hours, minutes, seconds = convert_seconds(total_seconds)
    
    # Выводим результат
    print("\n--- РЕЗУЛЬТАТ ---")
    print("Всего секунд:", total_seconds)
    print("Часы:", hours)
    print("Минуты:", minutes)
    print("Секунды:", seconds)
    print()
    print(f"Форматированное время: {hours}:{minutes:02d}:{seconds:02d}")
else:
    print("ОШИБКА! Введите только целое положительное число.")

print()
input("\nНажмите Enter для перехода к заданию 3...")
print("\n" * 2)


# =====================================================
# ЗАДАНИЕ 3: Сумма n + nn + nnn
# =====================================================

print("=" * 50)
print("ЗАДАНИЕ 3")
print("=" * 50)

# Запрашиваем число от 1 до 9
n_input = input("Введите число от 1 до 9: ")

# Проверяем, что введена одна цифра
if n_input.isdigit() and len(n_input) == 1:
    n = int(n_input)
    
    # Проверяем диапазон
    if 1 <= n <= 9:
        # Формируем nn и nnn
        nn = int(str(n) * 2)   # например, "3" * 2 = "33", потом в число
        nnn = int(str(n) * 3)  # например, "3" * 3 = "333", потом в число
        
        # Суммируем
        result = n + nn + nnn
        
        # Выводим результат
        print("\n--- РЕЗУЛЬТАТ ---")
        print(f"Вы ввели: {n}")
        print(f"Вычисляем: {n} + {nn} + {nnn} = {result}")
    else:
        print("ОШИБКА! Число должно быть от 1 до 9.")
else:
    print("ОШИБКА! Введите ОДНУ цифру от 1 до 9.")

print("\n" + "=" * 50)
print("Конец программы")
print("=" * 50)
