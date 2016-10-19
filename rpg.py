#Brandon Fordham
#bf11c
#Midterm. Does not support multi-client networking capabilities
from __future__ import print_function  
from random import randint
import string
class Character:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)
        return self.name

class Player(Character):
    def __init__(self, name):
        self.leave = 0
        self.x = 0
        self.y = 2    
        self.fight = 0
        self.struggle = 0
        self.hp = 30
        self.atkval = 0
        self.damage = 8
        self.fight1 = 0
        self.run = 0
    def help(self):
        print("go [N, S, E or W]")
        print("quit")
        print("attack")
        print("health")
        print("help")

    def go(self):
        if(self.fight1 == 1):
            print("Can't run from a fight!")
        elif(input2 == "go N"):
            if((self.y == 0 and self.x == 0) or (self.y == 0 and self.x == 1) or (self.y == 0 and self.x == 2) or (self.y == 0 and self.x == 3) or (self.y == 0 and self.x == 4)):
                print("Ouch! You ran into the north wall!")
            else:
                self.y = self.y - 1
                if(matrix2[self.y][self.x] == "E"):
                    print("A wild evil robot has appeared. Prepare to attack!")
                    self.fight = 1
                    self.fight1 = 1
                elif(matrix2[self.y][self.x] == "B"):
                    print("You found your backpack! You won the game!")
                    self.leave = 1
                elif(matrix2[self.y][self.x] == "R"):
                    print("You fell into a rat trap! You lose the game!")
                    self.leave = 1
                matrix2[self.y][self.x] = "P"
        if(input2 == "go S"):
            if((self.y == 4 and self.x == 0) or (self.y == 4 and self.x == 1) or (self.y == 4 and self.x == 2) or (self.y == 4 and self.x == 3) or (self.y == 4 and self.x == 4)):
                print("Ouch! You ran into the south wall!")
            else:
                self.y = self.y + 1
                if(matrix2[self.y][self.x] == "E"): 
                    print("A wild evil robot has appeared. Prepare to attack!")
                    self.fight = 1
                    self.fight1 = 1
                elif(matrix2[self.y][self.x] == "B"):
                    print("You found your backpack! You won the game!")
                    self.leave = 1
                elif(matrix2[self.y][self.x] == "R"):
                    print("You fell into a rat trap! You lose the game!")
                    self.leave = 1
                matrix2[self.y][self.x] = "P"
        if(input2 == "go W"):
            if((self.y == 0 and self.x == 0) or (self.y == 1 and self.x == 0) or (self.y == 2 and self.x == 0) or (self.y == 3 and self.x == 0) or (self.y == 4 and self.x == 0)):
                print("Ouch! You ran into the west wall!")
            else:
                self.x = self.x -1
                if(matrix2[self.y][self.x] == "E"):
                    self.fight = 1
                    self.fight1 = 1
                    print("A wild evil robot has appeared. Prepare to attack!")
                elif(matrix2[self.y][self.x] == "B"):
                    print("You found your backpack! You won the game!")
                    self.leave = 1
                elif(matrix2[self.y][self.x] == "R"):
                    print("You fell into a rat trap! You lose the game!")
                    self.leave = 1
                matrix2[self.y][self.x] = "P"
        if(input2 == "go E"):
            if((self.y == 0 and self.x == 4) or (self.y == 1 and self.x == 4) or (self.y == 2 and self.x == 4) or (self.y == 3 and self.x == 4) or (self.y == 4 and self.x == 4)):
                print("Ouch! You ran into the east wall!")
            else:
                self.x = self.x + 1            
                if(matrix2[self.y][self.x] == "E"):
                    self.fight = 1
                    self.fight1 = 1
                    print("A wild evil robot has appeared. Prepare to attack!")        
                elif(matrix2[self.y][self.x] == "B"):
                    print("You found your backpack! You won the game!")
                    self.leave = 1
                elif(matrix2[self.y][self.x] == "R"):
                    print("You fell into a rat trap! You lose the game!")
                    self.leave = 1
                matrix2[self.y][self.x] = "P"       
  #      print(matrix2[self.y][self.x]) 
 #       print("selfynx are ", self.y, self.x)       

    def attack(self):
       
        val1 = player1.health
        if(self.fight == 0):
            print("There is nothing to attack!")
        else:            
            self.fight = 1
            self.atkval = self.atkval + 1
            print(charName, "attacks Evil Robot for", self.damage, "points of damage!")
            if(self.atkval == 2):
                print("Evil Robot has been defeated!")
                matrix2[self.y][self.x] = "P"
                self.fight = 0
                self.atkval = 0
                self.fight1 = 0
                print("You found a health potion! Plus 2 hp!")
                self.hp = self.hp + 2
            else:
                print("Evil Robot attacks", charName, "for", self.damage, "points of damage!")
            self.hp = self.hp - self.damage 
            if(self.hp == 0):
                print("You have died! Game over. ")
                self.leave = 1            
#        print(self.hp)
            
           
    def opponent_hp(self, opponent):	
        opponent.hp = opponent.hp - damage
            

    def quit(self):
        print("You chose to end the game!")
        self.leave = 1
                      

    def health(self):
        value1 = self.hp
        print(value1)

class CodeWarrior(Player):
    pass

class EvilRobot(Character):
    pass

class H4x0r(Player):
    pass
  
#classes end here.

a = 5
b = 5

matrix = [["x" for x in range(a)] for y in range(5)]
matrix2 = [["x" for x in range(a)] for y in range(5)]
#Formatting ends here

print("Enter your character's name: ", end = "")
charName = raw_input()
print("Are you a CodeWarrior or 1337H4x0r? Enter [c] or [h]: ", end = "")
input1 = raw_input()
print("Your journey awaits...Good luck", charName, "!")
n = 0
bag = 0
matrix[2][0] = "P"
matrix2[2][0] = "P"
rat = 0
y = 6
x = 6


while(rat == 0):
    y = randint(0,4)
    x = randint(0,4)
    if((y != 2 and x != 0) and rat == 0):
        matrix[y][x] = "R"
        matrix2[y][x] = "R"
        rat = 1
        break 
count = 0
robo1 = 0
robo2 = 0
robo3 = 0
robo4 = 0
robo5 = 0
a = 0 
b = 0
b1 = 6
b11 = 6
r1 = 6
r11 = 6
r2 = 6
r22 = 6
r3 = 6
r33 = 6
r4 = 6
r44 = 6
r5 = 6
r55 = 6
#print("y and x are ", y, x)
while(count == 0):
    a = randint(0,4)
    b = randint(0,4)
   # print("a and b: ", a, b)
    
    if((a != y or b != x) and (a != 2 or b != 0 ) and (bag == 0)):
        b1 = a
        b11 = b
        matrix[a][b] = "B"
        matrix2[a][b] = "B"
        bag = 1
    elif((a != y or b !=x) and  (a!= 2 or b != 0) and (robo1 == 0) and (a != b1 or b != b11)):
        robo1 = 1
        r1 = a
        r11 = b
        matrix[r1][r11] = "E"
        matrix2[r1][r11] = "E"
      
        #print("r1 is now in", r1, r11)
    elif((a != y or b !=x) and ( a!= 2 or b != 0) and(robo1==1) and (robo2 == 0) and (a != r1 or b != r11) and (a != b1 or b != b11)):
        robo2 = 1
        r2 = a
        r22 = b
        matrix[r2][r22] = "E"
        matrix2[r2][r22] = "E"
       # print("r2 is now in", r2, r22)
    elif((a != y or b !=x) and ( a!= 2 or b != 0) and(robo2==1) and (robo3== 0) and (a != r1 or b != r11) and (a != r2 or b != r22) and (a != b1 or b != b11)):
        robo3 = 1
        r3 = a
        r33 = b
        matrix[r3][r33] = "E"
        matrix2[r3][r33] = "E"
      #  print("r3 is now in", r3, r33)
    elif((a != y or b !=x) and ( a!= 2 or b != 0) and(robo3==1) and (robo4== 0) and (a != r1 or b != r11) and (a != r2 or b != r22) and (a != r3 or b != r33) and (a != b1 or b != b11)):
     #   print("robo4: count is now increased")
        robo4 = 1
        r4 = a
        r44 = b
        matrix[r4][r44] = "E"
        matrix2[r4][r44] = "E"
    #    print("r4 is now in", r4, r44)
    elif((a != y or b !=x) and ( a!= 2 or b != 0) and(robo4==1) and (robo5==0) and (a != r1 or b != r11) and (a != r2 or b != r22) and (a != r3 or b != r33) and (a != r4 or b != r44) and (a != b1 or b != b11)):
        robo5 = 1
        r5 = a
        r55 = b
        matrix[r5][r55] = "E"
        matrix2[r5][r55] = "E"
   #     print("r5 is now in", r5, r55)
        count = 1
        break
    
    
    
                
"""
print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[0][4])
print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3], matrix[1][4])
print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3], matrix[2][4])
print(matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3], matrix[3][4])
print(matrix[4][0], matrix[4][1], matrix[4][2], matrix[4][3], matrix[4][4])
"""
quit1 = 0
codehaxor = Character(charName)
#player1 = Player(charName)
player1 = Player(charName)
while(player1.leave == 0):
    input2 = raw_input()
    if(input2 == "help"):
        player1.help()
    elif(input2 == "health"):
        player1.health()
    elif(input2 == "attack"):
        player1.attack()
    elif(input2 == "quit"):
        player1.quit()
        quit = 10
    elif(input2 == "go N" or input2 == "go S" or input2 == "go E" or input2 == "go W"):
        player1.go() 
   #     print("we did go")

    quit1 = quit1 + 1
"""
    print("****************************************")
    print(matrix2[0][0], matrix2[0][1], matrix2[0][2], matrix2[0][3], matrix2[0][4])
    print(matrix2[1][0], matrix2[1][1], matrix2[1][2], matrix2[1][3], matrix2[1][4])
    print(matrix2[2][0], matrix2[2][1], matrix2[2][2], matrix2[2][3], matrix2[2][4])
    print(matrix2[3][0], matrix2[3][1], matrix2[3][2], matrix2[3][3], matrix2[3][4])
    print(matrix2[4][0], matrix2[4][1], matrix2[4][2], matrix2[4][3], matrix2[4][4])
    print("*****************************************")
"""







