import itertools

items = {
    'r': (3, 25),  # Винтовка
    'p': (2, 15),  # Пистолет
    'a': (2, 15),  # Боекомплект
    'm': (2, 20),  # Аптечка
    'i': (1, 5),   # Ингалятор
    'k': (1, 15),  # Нож
    'x': (3, 20),  # Топор
    't': (1, 25),  # Оберег
    'f': (1, 15),  # Фляжка
    'd': (1, 10),  # Антидот
    's': (2, 20),  # Еда
    'c': (2, 20)   # Арбалет
}

 
max_cells = 9  # 3x3 ячейки
initial_survival_points = 10   

 
def can_survive(selection):
    total_points = 0
    cell_count = 0
    has_inhaler = 'i' in selection
    has_antidot = 'd' in selection

    for item in selection:
        cells, points = items[item]
        total_points += points
        cell_count += cells
    
    # Проверка не превышает ли количество ячеек
    if cell_count > max_cells:
        return None, 0
    
    
    total_points += initial_survival_points - (10 * len(selection))  
    
     
    if not (has_inhaler or has_antidot):
        return None, 0
    return total_points, cell_count

 
def find_best_inventory():
    best_inventory = None
    best_score = float('-inf')

    for r in range(1, len(items) + 1):
        for selection in itertools.combinations(items.keys(), r):
            total_points, cell_count = can_survive(selection)
 
            if total_points is not None and total_points > best_score:
                best_score = total_points
                best_inventory = selection
    return best_inventory, best_score

 
best_inventory, best_score = find_best_inventory()
 

if best_inventory:
    inventory_matrix = [[' ' for _ in range(3)] for _ in range(3)]
    
     
    for index, item in enumerate(best_inventory):
        row, col = divmod(index, 3)
        inventory_matrix[row][col] = item

    print("Итоговый инвентарь:")
    for row in inventory_matrix:
        print("[" + "][".join(row) + "]")

    print("Итоговые очки выживания:", best_score)
else:
    print("Не удалось собрать инвентарь с положительными очками выживания.")