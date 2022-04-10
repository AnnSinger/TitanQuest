heroes_health = 1000
print('Здоровье Героя = ' + str(heroes_health))
heroes_dmg = 100
print('Урон Героя = ' + str(heroes_dmg))
titan_health = 100
print('Здоровье Титана = ' + str(titan_health))
titan_dmg = 30
print('Урон Титана = ' + str(titan_dmg))
titan_helper_health = 60
print('Здоровье помощника Титана = ' + str(titan_health))
titan_helper_dmg = 20
print('Урон помощьника Титана = ' + str(titan_helper_dmg))

while True:
    if heroes_health < 0:
        print('Ваш герой мертв')
        break
    if titan_health < 0:
        print('Титан мертв')
    if titan_health < 0:
        print('Помощник Титана мертв')

    user_input = input('Кого будете атаковать? ')

    if user_input == 'Titan':
        titan_health = titan_health - heroes_dmg
        print('Здоровье Титана = ' + str(titan_health))
    elif user_input == 'Titan helper':
        titan_helper_health = titan_helper_health - heroes_dmg
        print('Здоровье помощника Титана = ' + str(titan_helper_health))
    else:
        print('Неправильно введено имя')
        user_input = input('Кого будете атаковать? ')

    if titan_health > 0:
        heroes_health = heroes_health - titan_dmg
        print('Секира Титана проносится над головой Героя')
        print('Здоровье Героя = ' + str(heroes_health))

    if titan_helper_health > 0:
        heroes_health = heroes_health - titan_helper_dmg
        print('Помощник Титана коварно бьет вас в спину')
        print('Здоровье Героя = ' + str(heroes_health))
