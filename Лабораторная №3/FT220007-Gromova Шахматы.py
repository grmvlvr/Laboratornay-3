def is_same_color(k, l, m, n):
    return (k + l) % 2 == (m + n) % 2

# Функция для проверки, угрожает ли фигура полю (m, n)
def threatens(k, l, m, n, piece):
    if piece == "ферзь":
        return k == m or l == n or abs(k - m) == abs(l - n)
    elif piece == "ладья":
        return k == m or l == n
    elif piece == "слон":
        return abs(k - m) == abs(l - n)
    elif piece == "конь":
        return (abs(k - m) == 2 and abs(l - n) == 1) or (abs(k - m) == 1 and abs(l - n) == 2)
    else:
        return False

# Функция для проверки, можно ли попасть на поле (m, n) одним ходом
def can_reach(k, l, m, n, piece):
    if piece == "ферзь" or piece == "ладья":
        return k == m or l == n
    elif piece == "слон":
        return abs(k - m) == abs(l - n)
    else:
        return False

# Функция для определения поля, на которое можно попасть за два хода
def get_two_step_destination(k, l, m, n, piece):
    if piece == "ферзь" or piece == "ладья":
        return (m, n)
    elif piece == "слон":
        return (m + (k - m) // 2, n + (l - n) // 2)
    else:
        return None

# Ввод данных от пользователя
k = int(input("Введите номер вертикали для первого поля (1-8): "))
if k < 1 or k > 8:
    print("Номер вертикали должен быть в диапазоне от 1 до 8")
    exit()

l = int(input("Введите номер горизонтали для первого поля (1-8): "))
if l < 1 or l > 8:
    print("Номер горизонтали должен быть в диапазоне от 1 до 8")
    exit()

m = int(input("Введите номер вертикали для второго поля (1-8): "))
if m < 1 or m > 8:
    print("Номер вертикали должен быть в диапазоне от 1 до 8")
    exit()

n = int(input("Введите номер горизонтали для второго поля (1-8): "))
if n < 1 or n > 8:
    print("Номер горизонтали должен быть в диапазоне от 1 до 8")
    exit()

piece = input("Введите название фигуры (ферзь, ладья, слон, конь): ").lower()
valid_pieces = ["ферзь", "ладья", "слон", "конь"]

if piece not in valid_pieces:
    print("Неверное название фигуры. Пожалуйста, введите корректное название.")
    exit()
    
# Проверки и вывод результатов
if is_same_color(k, l, m, n):
    print("Поля одного цвета")
else:
    print("Поля разного цвета")

if threatens(k, l, m, n, piece):
    print(f"{piece.capitalize()} угрожает полю ({m}, {n})")
else:
    print(f"{piece.capitalize()} не угрожает полю ({m}, {n})")

if can_reach(k, l, m, n, piece):
    print(f"Можно попасть с ({k}, {l}) на ({m}, {n}) одним ходом")
else:
    destination = get_two_step_destination(k, l, m, n, piece)
    if destination:
        print(f"Для попадания с ({k}, {l}) на ({m}, {n}) нужно два хода, первый - ({destination[0]}, {destination[1]})")
    else:
        print(f"Нельзя попасть с ({k}, {l}) на ({m}, {n}) за два хода")
