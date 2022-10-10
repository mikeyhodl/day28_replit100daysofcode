import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat


print("          ⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()

c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("          ⚔️ BATTLE TIME ⚔️")
  print()
  print("          The battle begins!")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(c1Strength - c2Strength) + 1

  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()

  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    

time.sleep(1)
os.system("clear")
print("              ⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")





playGame = "yes"

while True:
  os.system("clear")
  time.sleep(1)
  
  print("⚔️ Character Generator ⚔️")
  time.sleep(1)
  character_1 = character_builder()
  health_1 = health_stats()
  strength_1 = strength_stats()
  print(character_1)
  time.sleep(1)
  print("HEALTH:", health_1)
  time.sleep(1)
  print("STRENGTH:", strength_1)
  time.sleep(1)
  
  print("Who are they battling?")
  time.sleep(1)
  character_2 = character_builder()
  health_2 = health_stats()
  strength_2 = strength_stats()
  print(character_2)
  time.sleep(1)
  print("HEALTH:", health_2)
  time.sleep(1)
  print("STRENGTH:", strength_2)
  time.sleep(1)
  
  battle_counter = 0

  while True:
    battle_counter += 1
    os.system("clear")
    print("⚔️ Battle time ⚔️")
    time.sleep(1)
    
    if battle_counter == 1:
      print("The battle begins!")
    else :
      print("The battle continues")
    
    time.sleep(2)
  
    character_1_dice = rollDice(6)
    character_2_dice = rollDice(6)
    health_damage = damage(strength_1, strength_2)
  
    if character_1_dice > character_2_dice :
      print(character_1," wins round ",battle_counter)
      print(character_2," takes a hit with ",health_damage," damage")
      health_2 -= health_damage
    elif character_2_dice > character_1_dice :
      print(character_2," wins round ",battle_counter)
      print(character_1," takes a hit with ",health_damage," damage")
      health_1 -= health_damage
    else:
      print("It's a draw")

    time.sleep(2)

    print(character_1)
    print("HEALTH : ", health_1)
    time.sleep(2)
    print(character_2)
    print("HEALTH : ", health_2)

    time.sleep(2)

    if health_1 <= 0 :
      print("Oh no ", character_1, " has died!")
      print(character_2," has destroyed ", character_1, " in ",battle_counter," rounds")
      break
    elif health_2 <= 0:
      print("Oh no ", character_2, " has died!")
      print(character_1," has destroyed ", character_2, " in ",battle_counter," rounds")
      break
    else :
      print("And they are both standing for the next round!")
      
      time.sleep(2)
      continue
  
  playGame = input("Start over?:")
  if playGame == "yes":
    continue
  else:
    break