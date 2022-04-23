#Settings

def input_character():
    character_name = input('Введите Имя: ')
    character_health = int(input('Введите Здоровье: '))
    character_dmg = int(input('Введите Урон: '))
    return [character_name, character_health, character_dmg]

print('Введите статы героя...')
hero = input_character()
hero_aura_enabled = False
hero_aura_power = 1

list_of_allies = []
list_of_enemies = []

while True:
    command = input('Введите команду ')
    if command == 'союзник':
        print('Введите Союзника ')
        ally = input_character()
        list_of_allies.append(ally)
    elif command == 'враг':
        print('Введите Врага ')
        enemy = input_character()
        list_of_enemies.append(enemy)
    elif command == 'выход':
        break
    else:
        print('Нет такой команды')

print(hero)
print(list_of_allies)
print(list_of_enemies)

#Gameplay
print('Вы в игре')
while True:
    if hero[1] < 0:
        print('Ваш герой мертв')
        break

    if len(list_of_allies) == 0:
        print('Ваши союзники мертвы')
        # break

    if len(list_of_enemies) == 0:
        print('Ваши противники мертвы')
        break

    if hero_aura_enabled == True:
        print('Смердящая аура активна, хорошим будет хорошо, плохим - плохо')

        for ally in list_of_allies:
            ally[1] += 5 * hero_aura_power

        for enemy in list_of_enemies:
            enemy[1] -= 10 * hero_aura_power
            enemy[2] -= 2 * hero_aura_power

        hero_aura_power += 1

    print(list_of_allies)
    print(list_of_enemies)

    command = input('Кого будете атаковать? ')
    if command.isdigit() == True:
        if 0 <= int(command) < len(list_of_enemies):
            list_of_enemies[int(command)][1] -= hero[2]
            print('В результате удара были нанесены удары по ' + str(
                list_of_enemies[int(command)][0]) + ' У него осталось ' + str(list_of_enemies[int(command)][1]) + ' здоровья')
            if list_of_enemies[int(command)][1] <= 0:
                list_of_enemies.pop(int(command))
    else:
        if command == 'аура':
            hero_aura_enabled = True

    for ally_elem in list_of_allies:
        list_of_enemies[0][1] -= ally_elem[2]

    print('Удар пришёлся по врагу ' + str(list_of_enemies[0][0]) + ' У него осталось ' + str(list_of_enemies[0][1]) + ' здоровья')
    if list_of_enemies[0][1] <= 0:
        list_of_enemies.pop(0)

    for enemy_elem in list_of_enemies:
        list_of_allies[0][1] -= enemy_elem[2]

    print('Удар пришёлся по союзнику ' + str(list_of_allies[0][0]) + 'У него осталось ' + str(list_of_allies[0][1]) + ' здоровья')
    if list_of_allies[0][1] <= 0:
        list_of_allies.pop(0)

