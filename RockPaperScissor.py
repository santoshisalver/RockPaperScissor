# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:26:48 2024

@author: santo
"""

def rock_paper_scissor(num1,num2,bit1,bit2):
    if bit1 >= len(num1) or bit2 >= len(num2):
      print("Invalid bit position!")
      return
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if (player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissors"):
        print("player one wins!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissors"):
        print("player two wins!!")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("player two wins!!")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissors"):
        print("player one wins!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("player one wins!!")
    elif(player_one[p1]=="Scissors" and player_two[p2]=="Rock"):
        print("player one wins!!")
player_one={0:'Rock',1:'Paper',2:'Scissors'}
player_two={0:'Paper',1:'Scissors',2:'Rock'}
while(1):
    num1=input("Player one,Enter your Choice: ")
    num2=input("Player two,Enter your Choice: ")
    bit1=int(input("Player one,Enter the secret bit position: "))
    bit2=int(input("Player two,Enter the secret bit position: "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue?y/n: ")
    if(ch=='n'):
        break