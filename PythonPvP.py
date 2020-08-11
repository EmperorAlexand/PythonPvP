#Imports
import random
import math
import sys

#Player lists
players = []
playernames = []

#Items

#Weapons
bad_weapons = ['Wooden axe', 'Stone axe', 'baseball bat', 'frying pan', 'Wooden spear', 'Wooden sword']
bad_weapons_atk = [3, 5, 2, 4, 3, 4]
medium_weapons = ['Iron axe', 'Stone sword', 'Bow and arrow', 'Stone spear']
medium_weapons_atk = [7, 6, 6, 5]
good_weapons = ['Iron sword', 'Crossbow', 'Golden sword', 'Iron Spear', 'Golden axe']
good_weapons_atk = [9, 8, 10, 8, 8]
superior_weapons = ['Platinum sword', 'Uranium sword', 'Ruby axe', 'Emerald axe', 'Saphire axe']
superior_weapons_atk = [12, 11, 12, 11, 10]
weapons = [bad_weapons, medium_weapons, good_weapons, superior_weapons]

#Armor
bad_armor = ['Leather armor', 'Rubber armor', 'Coal Armor', 'Bronze armor', 'Aluminum armor']
bad_armor_dfn = [2, 2, 1, 3, 3]
medium_armor = ['Chainmail', 'Iron armor', 'Silver armor']
medium_armor_dfn = [4, 5, 6]
good_armor = ['Golden armor', 'Volfram armor']
good_armor_dfn = [7, 7]
superior_armor = ['Orphan armor', 'Uranium armor']
superior_armor_dfn = [10, 9]
armor = [bad_armor, medium_armor, good_armor, superior_armor]

#Player class
class Player:
    hp = 100
    max_hp = 100
    base_atk = 5
    base_dfn = 1
    base_spd = 5
    level = 1
    exp = 0
    max_exp = 10
    name = ''
    weapon = ''
    weapon_atk = 0
    armor = ''
    armor_dfn = 0
    total_atk = base_atk + weapon_atk
    total_dfn = base_dfn + armor_dfn
    total_spd = base_spd
    weapon_bless = False
    armor_bless = False

#Warning
try:
    color = sys.stdout.shell
    IDLE = True
except AttributeError:
    IDLE = False

#Rounds
crn_player = 1
session = 1

#Functions

#Level up
def Level_up(player):
    if player.exp >= player.max_exp:
        player.exp = player.exp - player.max_exp
        player.level += 1
        player.max_hp += 5
        print('You leveled up! Level ' + str(player.level) + '!')
        print('Your max hp increased by 5! Yor max hp is now', str(player.max_hp) + '.')

#Set new player
def New_player():
    global crn_player
    global session
    Level_up(players[crn_player - 1])
    if players[crn_player - 1] != players[-1]:
        crn_player += 1
    else:
        crn_player = 1
        session += 1
        print('---------------------')
        print("Round " + str(session) + "!\n")
        if session <= 10:
            print(11 - session, 'rounds until you can start fighting!')

#Set full stats
def Set_total(player):
    player.total_atk = player.base_atk + player.weapon_atk
    player.total_dfn = player.base_dfn + player.armor_dfn
    player.total_spd = player.base_spd

#Game over
def Game_over():
    global pn
    for i in range(len(players)):
        try:
            if players[i].hp <= 0:
                dead = players[i]
                print('Player', dead.name, 'was defeated!')
                players.remove(dead)
                playernames.remove(dead.name)
                pn -= 1
        except IndexError:
            i = 0

#Win
def Win():
    global playing
    if len(players) == 1:
        if IDLE == True:
            color.write('\nPlayer ' + players[0].name + ' has won!\n', 'KEYWORD')
            color.write('CONGRATULATIONS!\n', 'STRING')
        else:
            print('\n' + players[0].name, 'has won!\n')
            print('CONGRATULATIONS!')
        playing = False

#Commands

#Stats
def Help():
    if IDLE == True:
        color = sys.stdout.shell
        print('Welcome to the PythonPvP help page!\n')
        print('Here\'s a list of the availible commands.\nThe red commands will end your turn.\nThe green commands will not.\n')
        color.write('Help ', 'STRING')
        print('(Shows the help page)')
        color.write('Stats ', 'STRING')
        print('(Shows a players stats)')
        color.write('Attack ', 'COMMENT')
        print('(Attack another player)')
        color.write('Heal ', 'COMMENT')
        print('Heal yourself if you are damaged')
        color.write('Train ', 'COMMENT')
        print('(Train to increase your attack or speed)')
        color.write('Meditate ', 'COMMENT')
        print('(Meditate to earn exp)')
        color.write('Scavenge ', 'COMMENT')
        print('(Scavenge to find weapons and armor)')
        color.write('Enchant ', 'STRING')
        print('(Enchant your gear to make it stronger)')
        color.write('Sacrifice ', 'STRING')
        print('(Sacrifice to a deity for better stats)')
        color.write('Bless ', 'COMMENT')
        print('(Bless your gear to make it even better!)')
    else:
        print('Welcome to the PythonPvP help page!\n')
        print('Here\'s a list of the availible commands.\nThe commands with an \'x\' at the end will end your turn.\nThe other ones will not.\n')
        print('Help (Shows the help page)')
        print('Stats (Shows a players stats)')
        print('Attack (Attack another player) x')
        print('Heal (Heal yourself if you are damaged) x')
        print('Train (Train to increase your attack or speed) x')
        print('Meditate (Meditate to earn exp) x')
        print('Scavenge (Scavenge to find weapons and armor) x')
        print('Enchant (Enchant your gear to make it stronger) x')
        print('Sacrifice (Sacrifice to a deity for better stats)')
        print('Bless (Bless your gear to make it even better!) x')

#Stats        
def Stats():
    print('Which players stats do you want to view?\nAvailible players:', playernames)
    inp = input()
    try:
        if inp in playernames:
            goal = players[playernames.index(inp)]
        else:
            goal = players[int(inp) - 1]
        print('Showing', goal.name + ' (Level ' + str(goal.level) + ') \'s stats.')
        print('Hp: (' + str(goal.hp) + '/' + str(goal.max_hp) + ')')
        print('Total attack:', goal.total_atk)
        print('Total defense:', goal.total_dfn)
        print('Total speed:', goal.total_spd)
        print('Weapon:', goal.weapon, '(' + str(goal.weapon_atk), 'atk)')
        print('Armor:', goal.armor, '(' + str(goal.armor_dfn), 'dfn)')
        print('Exp until level up:', goal.max_exp - goal.exp)

    except IndexError:
        print('That player doesn\'t exist!')
        
#Attack
def Attack(atk_player):
    if session > 10:
        print('Who do you want to attack?\nAvailible players:', playernames)
        inp = int(input('(Input the index of the player)\n'))
        dfn_player = players[inp - 1]
        if random.randint(1, 100) <= dfn_player.total_spd:
            dfn_player.exp += 3
            print(dfn_player.name, 'dodges your attack!')
            print(dfn_player.name, 'gains 3 xp!')
        elif random.randint(1, 100 + int(atk_player.total_atk / 2)) <= atk_player.total_atk:
            atk_player.exp += 5
            print('You strike', dfn_player.name, 'with a critical hit!')
            print(dfn_player.name, 'blocks', dfn_player.total_dfn, 'damage!')
            if atk_player.total_atk * 2 - dfn_player.total_dfn > 0:
                print(atk_player.total_atk * 2 - dfn_player.total_dfn, 'damage dealt!')
                dfn_player.hp = dfn_player.hp - (atk_player.total_atk * 2 - dfn_player.total_dfn)
            else:
                print('Zero damage dealt!')
            print('You gained 5 exp!')
        else:
            atk_player.exp += 2
            print('You strike', dfn_player.name + "!")
            print(dfn_player.name, 'blocks', dfn_player.total_dfn, 'damage!')
            if atk_player.total_atk * 2 - dfn_player.total_dfn > 0:
                print(atk_player.total_atk - dfn_player.total_dfn, 'damage dealt!')
                dfn_player.hp = dfn_player.hp - (atk_player.total_atk - dfn_player.total_dfn)
            else:
                print('Zero damage dealt!')
            print('You gained 2 exp!')
        print('Your hp:', atk_player.hp)
        print(dfn_player.name + '\'s hp:', dfn_player.hp)
        New_player()
    else:
        print('The preparation rounds aren\'t over yet!')
        print(11 - session, 'rounds left!')

#Heal
def Heal(player):
    heal = 5 + random.randint(0, player.level + 1)
    if player.hp == player.max_hp:
        print('You are alredy at max hp!')
    else:
        if heal > player.max_hp - player.hp:
            heal = player.max_hp - player.hp
            player.hp += heal
            print('You healed', heal, 'hp!')
            print('You are now at max hp.')
        else:
            player.hp += heal
            print('You healed', heal, 'hp!')
            print('You are now at', player.hp, 'hp')
        New_player()

#Train
def Train(player):
    if random.randint(1, 10) == 1:
        player.base_atk += 1
        player.base_spd += 2
        player.exp += 5
        print('You train very successfully! +1 Attack and +2 Speed!')
        print('5 exp gained!')
    elif random.randint(1, 10) <= 8:
        player.exp += 3
        if random.randint(1, 2) == 1:
            player.base_atk += 1
            print('You train successfully! +1 Attack!')
        else:
            player.base_spd += 2
            print('You train successfully! +2 Speed!')
    else:
        print('You train unsuccessfully.')
    New_player()
    Set_total(player)

#Meditate
def Meditate(player):
    if random.randint(1, 50) <= player.level:
        player.exp += 10
        print('You meditate with full concentration.')
        print('10 exp gained!')
    else:
        player.exp += 7
        print('You meditate.')
        print('7 exp gained!')
    New_player()

#Scavenge
def Scavenge(player):
    print('You scavenge for weapons and armor...')
    seed = random.randint(1, 100)
    if random.randint(1, 2) == 1:
        stat = 'attack'
        obj = 'weapon'
        if seed < 5:
            result = random.choice(superior_weapons)
            sort = 'superior'
            xnum = superior_weapons.index(result)
            num = superior_weapons_atk[xnum]
        elif seed < 20:
            result = random.choice(good_weapons)
            sort = 'good'
            xnum = good_weapons.index(result)
            num = good_weapons_atk[xnum]
        elif seed < 50:
            result = random.choice(medium_weapons)
            sort = 'medium'
            xnum = medium_weapons.index(result)
            num = medium_weapons_atk[xnum]
        else:
            result = random.choice(bad_weapons)
            sort = 'bad'
            xnum = bad_weapons.index(result)
            num = bad_weapons_atk[xnum]
    else:
        stat = 'defense'
        obj = 'armor'
        if seed < 5:
            result = random.choice(superior_armor)
            sort = 'superior'
            xnum = superior_armor.index(result)
            num = superior_armor_dfn[xnum]
        elif seed < 20:
            result = random.choice(good_armor)
            sort = 'good'
            xnum = good_armor.index(result)
            num = good_armor_dfn[xnum]
        elif seed < 50:
            result = random.choice(medium_armor)
            sort = 'medium'
            xnum = medium_armor.index(result)
            num = medium_armor_dfn[xnum]
        else:
            result = random.choice(bad_armor)
            sort = 'bad'
            xnum = bad_armor.index(result)
            num = bad_armor_dfn[xnum]
            
    print('You found a ' + result + '! This is a', sort + '-classed', obj, 'with', num, stat + ".")

    if obj == 'armor':
        if player.armor == '':
            player.armor = result
            player.armor_dfn = num
            print('You currently have no armor equipped.')
            print('You equipped the', result + '.')
            Set_total(player)
        else:
            print('You are already using', player.armor, 'with', player.armor_dfn, 'defense points.')
            switch = input('Do you want to use the ' + result + ' or sell it? (keep/sell)\n')
            switch = switch.upper()
            if switch == 'KEEP':
                player.armor = result
                player.armor_dfn = num
                print('You kept the', player.armor + '.')
                Set_total(player)
            elif switch == 'SELL':
                if sort == 'bad':
                    player.exp += 3
                    print('You sold it for 3 exp.')
                elif sort == 'medium':
                    player.exp += 5
                    print('You sold it for 5 exp.')
                elif sort == 'good':
                    player.exp += 7
                    print('You sold it for 7 exp.')
                elif sort == 'superior':
                    player.exp += 10
                    print('You sold it for 10 exp.')
            else:
                print('That was not an invalid input. You lost the found gear.')

    else:
        if player.weapon == '':
            player.weapon = result
            player.weapon_atk = num
            print('You currently have no weapon equipped.')
            print('You equipped the', result + '.')
            Set_total(player)
        else:
            print('You are already using', player.weapon, 'with', player.weapon_atk, 'attack points.')
            switch = input('Do you want to use the ' + result + ' or sell it? (keep/sell)\n')
            switch = switch.upper()
            if switch == 'KEEP':
                player.weapon = result
                player.weapon_atk = num
                print('You kept the', player.weapon + '.')
                Set_total(player)
            elif switch == 'SELL':
                if sort == 'bad':
                    player.exp += 3
                    print('You sold it for 3 exp.')
                elif sort == 'medium':
                    player.exp += 5
                    print('You sold it for 5 exp.')
                elif sort == 'good':
                    player.exp += 7
                    print('You sold it for 7 exp.')
                elif sort == 'bad':
                    player.exp += 10
                    print('You sold it for 10 exp.')
            else:
                print('That was not a valid input. You lost the found gear.')
                
    New_player()

#Enchant
def Enchant(player):
    gear = input('Do you want to enchant your armor or weapon? (Armor/Weapon)')
    gear = gear.upper()
    if gear == 'WEAPON':
        if player.weapon != '':
            if 'Enchanted' in player.weapon:
                print('You have already enchanted that weapon.')
            else:
                cost = int(math.ceil(player.weapon_atk / 2)) + 1
                final = input('Enchant ' + player.weapon + ' for the cost of ' + str(cost) + ' levels? (y/n)\n')
                if final == 'y' or 'Y' or 'Yes' or 'YES':
                    if player.level - cost >= 0:
                        player.level -= cost
                        print('You enchanted your', player.weapon + '!')
                        player.weapon = 'Enchanted ' + player.weapon
                        player.weapon_atk = int(player.weapon_atk * 1.5)
                        print('It now has', player.weapon_atk, 'attack!')
                        Set_total(player)
                    else:
                        print('You don\'t have enough levels!')
        else:
            print('You have no armor!')
                
    elif gear == 'ARMOR':
        if player.armor != '':
            if 'Enchanted' in player.armor:
                print('You have already enchanted that armor.')
            else:
                cost = int(math.ceil(player.armor_dfn / 2)) + 1
                final = input('Enchant ' + player.armor + ' for the cost of ' + str(cost) + ' levels? (y/n)\n')
                if final == 'y' or 'Y' or 'Yes' or 'YES':
                    if player.level - cost >= 0:
                        player.level -= cost
                        print('You enchanted your', player.armor + '!')
                        player.armor = 'Enchanted ' + player.armor
                        player.armor_dfn = int(player.armor_dfn * 1.5)
                        print('It now has', player.armor_dfn, 'defense!')
                        Set_total(player)
                    else:
                        print('You don\'t have enough levels!')
        else:
            print('You have no armor!')
    else:
        print('That is not a valid input.')

#Bless
def Sacrifice(player):
    deity = input('To whom do you want to sacrifice? (God/Satan)\n')
    deity = deity.upper()
    if deity == 'GOD':
        currency = input('What do you want to sacrifice for? (Atk/Spd)\n')
        currency = currency.upper()
        if currency == 'ATK':
            q = input('Sacrifice 5 hp for 1 atk? (y/n)')
            q = q.upper()
            if q == 'Y':
                player.base_atk += 1
                player.hp -= 5
                print('You sacrificed 5 hp to god.')
                print('1 atk gained!')
            elif q == 'N':
                print('Sacrifice cancelled.')
            else:
                print('Invalid input.')
        elif currency == 'SPD':
            q = input('Sacrifice 5 hp for 1 spd? (y/n)')
            q = q.upper()
            if q == 'Y':
                player.base_spd += 1
                player.hp -= 5
                print('You sacrificed 5 hp to god.')
                print('1 spd gained!')
            elif q == 'N':
                print('Sacrifice cancelled.')
            else:
                print('Invalid input.')
        else:
            print('That is not a valid input.')
    elif deity == 'SATAN':
        currency = input('What do you want to sacrifice for? (Dfn/Exp)\n')
        currency = currency.upper()
        if currency == 'DFN':
            q = input('Sacrifice 5 hp for 1 dfn? (y/n)')
            q = q.upper()
            if q == 'Y':
                player.base_dfn += 1
                player.hp -= 5
                print('You sacrificed 5 hp to satan.')
                print('1 dfn gained!')
            elif q == 'N':
                print('Sacrifice cancelled.')
            else:
                print('Invalid input.')
        elif currency == 'EXP':
            q = input('Sacrifice 5 hp for 5 Exp? (y/n)')
            q = q.upper()
            if q == 'Y':
                player.exp += 5
                player.hp -= 5
                print('You sacrificed 5 hp to satan.')
                print('5 exp gained!')
            elif q == 'N':
                print('Sacrifice cancelled.')
            else:
                print('Invalid input.')
        else:
            print('That is not a valid input.')
    else:
        print('That is not a deity!')
    Set_total(player)

#Bless
def Bless(player):
    bless = input('What do you want to bless? (weapon/armor)\n')
    bless = bless.upper()
    if bless == 'WEAPON':
        if 'Enchanted' in player.weapon:
            if player.weapon_bless == False:
                print('You pray for your', player.weapon + '...')
                if random.randint(1, 5) == 1:
                    print('Your prayer was answered!')
                    seed = random.randint(1, 10)
                    if seed == 1:
                        player.weapon_atk = int(math.ceil(player.weapon_atk * 2.5))
                        print('Your', player.weapon, 'got a godly blessing!')
                        player.weapon = 'Godly ' + player.weapon
                        player.weapon_bless = True
                    elif seed <= 4:
                        player.weapon_atk = int(math.floor(player.weapon_atk * 2))
                        print('Your', player.weapon, 'got an angelic blessing!')
                        player.weapon = 'Angelic ' + player.weapon
                        player.weapon_bless = True
                    else:
                        player.weapon_atk = int(math.ceil(player.weapon_atk * 1.5))
                        print('Your', player.weapon, 'got a normal blessing!')
                        player.weapon = 'Blessed ' + player.weapon
                        player.weapon_bless = True
                else:
                    print('Your prayer went unanswered.')
            else:
                print('That weapon is already blessed!')
        else:
            print('Unenchanted gear is unblessable!')
            
    elif bless == 'ARMOR':
        if 'Enchanted' in player.armor:
            if player.armor_bless == False:
                print('You pray for your', player.armor + '...')
                if random.randint(1, 5) == 1:
                    print('Your prayer was answered!')
                    seed = random.randint(1, 10)
                    if seed == 1:
                        player.armor_dfn = int(math.ceil(player.armor_dfn * 2.5))
                        print('Your', player.armor, 'got a godly blessing!')
                        player.armor = 'Godly ' + player.armor
                        player.armor_bless = True
                    elif seed <= 4:
                        player.armor_dfn = int(math.floor(player.armor_dfn * 2))
                        print('Your', player.armor, 'got an angelic blessing!')
                        player.armor = 'Angelic ' + player.armor
                        player.armor_bless = True
                    else:
                        player.armor_dfn = int(math.ceil(player.armor_dfn * 1.5))
                        print('Your', player.armor, 'got a normal blessing!')
                        player.armor = 'Blessed ' + player.armor
                        player.armor_bless = True
                else:
                    print('Your prayer went unanswered.')
            else:
                print('That armor is already blessed!')
        else:
            print('Unenchanted gear is unblessable!')
    else:
        print('That is not a valid option!')
    Set_total(player)
    New_player()

#Game

#Greeting
print('[--------------------------]')
print('⚔️ Welcome to PythonPvP! ⚔️')
print('[--------------------------]\n')
print('[|-------------------------------------|]')
print('Welcome to PythonPvP, a local pvp game coded entirely with python.\nPlay with up to 50 people, until only one man stands.\nYour goal is to defeat your opponents. Pretty simple.\nEvery player gets a turn to take action.\nImprove your stats, collect gear, and defeat your friends.\nIf you need help with the availible commands, type \'help\'.\nYou will have ten turns to prepare for battle before you can\nstart attacking other players. Good luck.\n      -Alexand')
print('[|-------------------------------------|]\n')

#Main boolean
playing = True

#Player number
while playing:
    while True:
        try:
            pn = int(input('How many players are participating?\n'))
            break
        except ValueError:
            print('That is not a number.')
    if pn <= 50 and pn > 1:
        break
    print("Error!")

#Create Players
while playing:
    for i in range(pn):
        players.append(Player())
        while True:
            crn_name = input("Player " + str(i + 1) + ", what is your name?\n")
            if crn_name not in playernames:
                playernames.append(crn_name)
                players[i].name = crn_name
                break
            else:
                print('That name is already taken!')
    break

#First round
print('---------------------')
print("Round " + str(session) + "!\n")
if session <= 10:
    print(11 - session, 'rounds until you can start fighting!')
    
#Main game loop
while playing:

    #Check if game over
    Game_over()

    #Take command
    for i in range(pn):
        if session == 1 and crn_player == 1 and len(players) > 1:
            print('Type help for help.')
        if len(players) > 1:
            cmd = input("Player " + playernames[crn_player - 1] + ", what is your next action?\n")
            cmd = cmd.upper()

            #Commands
            playing = players[crn_player - 1]
            print('---------------------')
            if cmd == 'HELP':
                Help()
            elif cmd == 'STATS':
                Stats()
            elif cmd == 'ATTACK':
                Attack(playing)
            elif cmd == 'HEAL':
                Heal(playing)
            elif cmd == 'TRAIN':
                Train(playing)
            elif cmd == 'MEDITATE':
                Meditate(playing)
            elif cmd == 'SCAVENGE':
                Scavenge(playing)
            elif cmd == 'ENCHANT':
                Enchant(playing)
            elif cmd == 'SACRIFICE':
                Sacrifice(playing)
            elif cmd == 'BLESS':
                Bless(playing)
            else:
                print('Invalid command!')

        #Terminate
        print('---------------------')

    #Win check
    Win()

#Finish
print('Game over.')
sys.exit()
