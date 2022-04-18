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

print(hero_name, hero_health, hero_dmg)
print(list_of_allies)
print(list_of_enemies)

#Gameplay
print('Вы в игре')
while True:
    if hero_health < 0:
        print('Ваш герой мертв')
        break

    if len(list_of_allies) == 0:
        print('Ваши союзники мертвы')
        break

    if len(list_of_enemies) == 0:
        print('Ваши противники мертвы')
        break

        print(list_of_allies)
        print(list_of_enemies)

    command = int(input('Кого будете атаковать? '))
    if command >= 0 and command < len(list_of_enemies):
        list_of_enemies[command][1] -= hero_dmg
        print('В результате атаки были нанесены удары по ' + str(list_of_enemies[0][0]) + '. У него осталось ' + str(list_of_enemies[0][1]) + ' здоровья')
        if list_of_enemies[command][1] <= 0:
            list_of_enemies.pop(command)

    for ally_elem in list_of_allies:
        list_of_enemies[0][1] -= ally_elem[2]

    print('Удар пришёлся по врагу ' + str(list_of_enemies[0][0]) + 'У него осталось ' + str(list_of_enemies[0][1]) + ' здоровья')
    if list_of_enemies[0][1] <= 0:
        list_of_enemies.pop(0)

    for enemy_elem in list_of_enemies:
        list_of_allies[0][1] -= enemy_elem[2]

    print('Удар пришёлся по союзнику ' + str(list_of_allies[0][0]) + 'У него осталось ' + str(list_of_allies[0][1]) + ' здоровья')
    if list_of_allies[0][1] <= 0:
        list_of_allies.pop(0)
