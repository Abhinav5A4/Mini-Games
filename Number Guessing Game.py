# The rules are quite simple:
# 1.User's guess should be between 1 and 100
# 2.On a user's first turn, if your guess is within 10 of the number, you will get hint "WARM! otherwise "COLD!"
# 3.On all subsequent turns, if a guess is closer to the number than the previous guess you will get hint "WARMER!" otherwise "COLDER!"
# 4.When the user guess equals the number, you won!

from random import randint
num=randint(0,101)
print(num)

guess_list=[]
  
while True: 
  a = input('enter a number between 1-100 \n')

  if int(a)>=1 and int(a)<=100:
    guess_list.append(int(a))
  else:
    print('num is out of bounds,please enter again \n')
    continue 

  if guess_list[-1]==num:
    print('you guessed it!')
    break
  elif abs(guess_list[0]-num) <=10 and len(guess_list) == 1:
    print('WARM')
  elif len(guess_list) == 1:
    print('COLD')
  else:
    if abs(num-guess_list[-2]) > abs(num-guess_list[-1]):
      print("Warmer")
    else:
      print("Colder")

print("Game over!")
