
import random
rock='''
     ________
___'    _____)
       (______)
       (______)
       (_____)
 __' __(____)
'''
paper='''
      ________
____ / _______)____
           ________)
           __________)
______     ________)
      \__________)
'''
scissor='''
      ________
____ / _______)____
           _________)
           __________)
______     ____)
      \_______)
'''
game=[rock,paper,scissor]
def playing(game):
    user_choice=int(input("enter the value ==> 0 for rock ==> 1 for paper ==> 2 for scissor "))
    if user_choice not in range(0,3):
        print("enter value is invalied")
    else:
        machine_choice=random.randint(0,2)
        print("user_choice",game[user_choice],"machine_choice",game[machine_choice])
        print("machine choice is",machine_choice)
        if(user_choice==machine_choice):
            print("-----------**game is Draw**----------   ")
        elif(user_choice +1==machine_choice):
            print("-----------**game won by machine**-----------")
        elif(user_choice==2 and machine_choice==0):
            print("------------**game won by machine**------------")
        else:
            print("------------**game won by user**-------------")
playing(game)
i=1
while(i>0):
    u=input("-->Do You want to continue the game yes/no ")
    if(u=="yes" or u=="YES"):
        playing(game)
        i=i+1
    else:
        break
        



