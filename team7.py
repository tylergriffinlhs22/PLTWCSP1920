####
# BETRAYAL ENGINE V0
####

team_name = 'CHLnGR'# Only 10 chars displayed
strategy_name = 'BETRAYAL V1.0.3'
strategy_description = '''fourth release of the betrayal engine'''
    
def move(my_history, their_history, my_score, their_score):
    import random
    '''doesnt do anything unless the enemy has betrayed, nothin works better tbh'''
    if not(my_history): #its round 1 start fast eat grass
        return 'b'
    elif 'b' in their_history:
        return 'b' # finish them
    else:
      if my_score < -150:
        return random.choice(["c","b","b"]) # if score low has higher chance of betrayal
      else:
        return random.choice(["c","c","b"]) # they havent betrayed yet, so randomly betray
        