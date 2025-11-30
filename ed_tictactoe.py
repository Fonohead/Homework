# Создаём игровое поле.
field = []
for i in range(4):
    field.append(["-"] * 4)

# Расставляем шкалу координат по сторонам поля.
field[0][0] = " "
field[1][0] = '1'
field[2][0] = '2'
field[3][0] = '3'
field[0][1] = '1'
field[0][2] = '2'
field[0][3] = '3'

# Функция вывода игрового поля.
def print_field():
    for row in field:
        print('  '.join(row))
    print()

# Проверка валидности хода.
def is_valid_move(row, col):
    return 1 <= row <= 3 and 1 <= col <= 3 and field[row][col] == "-"

# Выигрышные варианты.
def winning_line(player):
    # Строки.
    for i in range(1, 4):
        if field[i][1] == field[i][2] == field[i][3] == player:
            return True
    # Столбцы.
    for j in range(1, 4):
        if field[1][j] == field[2][j] == field[3][j] == player:
            return True
    # Диагонали.
    if field[1][1] == field[2][2] == field[3][3] == player:
        return True
    if field[1][3] == field[2][2] == field[3][1] == player:
        return True
    return False

# Проверка ничьи.
def is_draw():
    for i in range(1, 4):
        for j in range(1, 4):
            if field[i][j] == "-":
                return False
    return True

# Печатаем игровое поле и инструкции.
print("\n***** КРЕСТИКИ-НОЛИКИ *****")
print("\nЧтобы сделать ход, введите координаты строки и столбца в диапазоне от 1 до 3.")
print()
print_field()

# Начинает игрок 'x'.
current_player = 'x'

while True:

        # Ввод координат.
        row_coord = int(input(f"\nИгрок '{current_player}', введите координату строки: "))
        col_coord = int(input(f"Игрок '{current_player}', введите координату столбца: "))
        print()

        # Проверка валидности.
        if not is_valid_move(row_coord, col_coord):
            print("НЕВЕРНЫЙ ХОД! Координаты должны быть от 1 до 3, или возможно поле уже занято. "
                  "Ход не засчитан. Попробуйте снова.")
            print()
            print_field()
            continue

        # Размещаем символ.
        field[row_coord][col_coord] = current_player
        print_field()

        # Проверяем победу.
        if winning_line(current_player):
            print(f"ПОБЕДА ИГРОКА '{current_player}'!!! Игра окончена.")
            break

        # Проверяем ничью.
        if is_draw():
            print("НИЧЬЯ! Игра окончена.")
            break

        # Смена игрока.
        current_player = 'o' if current_player == 'x' else 'x'
