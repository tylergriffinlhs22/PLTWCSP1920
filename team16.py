import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 16' # Only 10 chars displayed
strategy_name = 'Average'
strategy_description = 'Counts amount of betrays and colludes in the history of the other team.'
    
def move(my_history, their_history, my_score, their_score):
    b = 0 
    c = 0
    for letter in their_history:
      if letter == 'b':
        b += 1
    for letter in their_history:
      if letter == 'c':
       c += 1
    if b > c:
      return 'b'
    else:
      return 'c'
    