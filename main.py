#Settings
hero_name = input('Введите Имя Героя ')
hero_health = int(input('Введите Здоровье Героя '))
hero_dmg = int(input('Введите Урон Героя '))

list_of_allies = []
list_of_enemies = []

while True:
    command = input('Введите команду ')
    if command == 'союзник':
        ally_name = input('Введите Имя Союзник ')
        ally_health = int(input('Введите Здоровье Союзника '))
        ally_dmg = int(input('Введите Урон Союзника '))
        list_of_allies.append([ally_name, ally_health, ally_dmg])
    elif command == 'враг':
        enemy_name = input('Введите Имя Врага ')
        enemy_health = int(input('Введите Здоровье Врага '))
        enemy_dmg = int(input('Введите Урон Врага '))
        list_of_enemies.append([enemy_name, enemy_health, enemy_dmg])
    elif command == 'выход':
        break
    else:
        print('Нет такой команды')
print(list_of_allies)
print(list_of_enemies)
