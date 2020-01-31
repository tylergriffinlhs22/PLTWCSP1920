####
# BETRAYAL ENGINE V0
####

team_name = 'CHLnGR'# Only 10 chars displayed
strategy_name = 'BETRAYAL V1.0.2'
strategy_description = '''third release of the betrayal engine'''
    
def move(my_history, their_history, my_score, their_score):
    import random
    '''doesnt do anything unless the enemy has betrayed, nothin works better tbh'''
    if not(my_history): #its round 1 start fast eat grass
        return 'b'
    elif 'b' in their_history:
        return 'b' # finish them
    else:
        return random.choice(["c","c","c","b"]) # they havent betrayed yet, so randomly betray
        