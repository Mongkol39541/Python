"""This is DocString"""

def attack(career, attack_power):
    """This is DocString"""
    if career == "sword":
        attack_power = 4
    elif career == "magic":
        attack_power = 2
    elif career == "sleep":
        attack_power = 0
    elif career == "master":
        attack_power = 9
    return attack_power

def enemy(enemy_name):
    """This is DocString"""
    enemy_life = 0
    enemy_attack = 0
    if enemy_name == "waddle dee":
        enemy_life = 2
        enemy_attack = 1
    elif enemy_name == "laser ball":
        enemy_life = 3
        enemy_attack = 2
    elif enemy_name == "waddle doo":
        enemy_life = 5
        enemy_attack = 3
    return enemy_life, enemy_attack

def calculate(life_force, enemy_life, enemy_name, kill):
    """This is DocString"""
    print("------------")
    if enemy_life <= 0 and life_force > 0:
        print("- " + str(enemy_name) + " had defeated -")
        kill += 1
    if life_force > 0:
        print(str(life_force) + " HP left")
        print("------------")
    elif life_force <= 0:
        print(str(life_force) + " HP left")
        print("GameOver!")
    return life_force, kill

def main():
    """This is DocString"""
    life_force = int(input())
    attack_power = 0
    kill = 0
    win = False
    while life_force > 0:
        career = str(input())
        career = career.lower()
        attack_power = attack(career, attack_power)
        enemy_name = str(input())
        enemy_name = enemy_name.lower()
        enemy_life, enemy_attack = enemy(enemy_name)
        if enemy_name == "heal":
            print("------------")
            life_force += 2
            print(str(life_force) + " HP left")
            print("------------")
        elif enemy_name == "none":
            print("------------")
            print(str(life_force) + " HP left")
            win = True
            break
        else:
            enemy_life -= attack_power
            life_force -= enemy_attack
            life_force, kill = calculate(life_force, enemy_life, enemy_name, kill)
    if win:
        print("Kirby won!")
    print("You had defeated " + str(kill) + " enemies")
    print("------------")
main()
