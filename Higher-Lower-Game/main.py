import art 
print(art.logo)
# print("Ok")
from game_data import data
import random as r
import os
 

end = False
 

# Pick Random Datas 
def get_random_acc():
  return r.choice(data)
  
# Function to print data 
def printData(C):
  C_name = C['name']
  C_desc = C['description']
  C_country = C['country']
  return f"{C_name}, {C_desc}, {C_country}"

#Check answer
def check_ans(guess, A_foll, B_foll):
  if A_foll > B_foll:
    return guess == "a"
  else:
    return guess == "b"
  
def print_competitor(A,B):
  print(f"A : {printData(A)}")
  print(art.vs)
  print(f"B : {printData(B)}")

def game():
  #declare score 
  score = 0
  Not_end = True
  
  #Starting 2 data
  A = get_random_acc()
  B = get_random_acc()
  if (A == B):
      B = get_random_acc()
    
  while Not_end:
    #Change the variables data 
    A = B
    B = get_random_acc()
    if (A == B):
      B = get_random_acc()
        
    print_competitor(A,B)
  
    #take guess from user and then check the follower count
    guess = input("Enter A or B ").lower()
    A_foll = A["follower_count"]
    B_foll = B["follower_count"]
    res = check_ans(guess,A_foll,B_foll)
  
    #if its true print
    if res:
      score = score + 1
      print(f"You win ! Score is {score} ")
    else:
      print(f"Sorry ! You Loose Score is {score} ")
      Not_end = False
  
game()


    
